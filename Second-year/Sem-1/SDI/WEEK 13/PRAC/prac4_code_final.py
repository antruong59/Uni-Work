import abc
import io


class AggregationOperation(metaclass=abc.ABCMeta):

    def __init__(self, data):
        self.data = data

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError


class SumAggregation(AggregationOperation):

    def execute(self):
        return sum(self.data)


class AverageAggregation(AggregationOperation):

    def execute(self):
        count = len(self.data)
        return sum(self.data)/count if count > 0 else 0


class CountAggregation(AggregationOperation):

    def execute(self):
        return len(self.data)


class OperationFactory:

    def __init__(self):
        self.aggregation_operations = dict()

    def register_operation(self, identifier, operation):
        self.aggregation_operations[identifier] = operation

    def get_operation(self, identifier):
        if identifier not in self.aggregation_operations:
            raise ValueError(f'Invalid operation "{identifier}"')
        return self.aggregation_operations[identifier]

    def create_operation(self, identifier, data):
        operation_class = self.get_operation(identifier)
        operation = operation_class(data)
        return operation


class AggregationTableParser:

    def __init__(self, factory):
        self.operations_factory = factory

    def split_row_fields(self, row):
        if not row:
            return []
        fields = [field.strip() for field in row.split(',')]
        return fields

    def parse_number(self, value_string):
        return float(value_string)

    def parse_operation_and_data(self, row):
        fields = self.split_row_fields(row)
        if not fields:
            raise ValueError('Empty row')
        operation = fields[0]
        data = [self.parse_number(value_string) for value_string in fields[1:]]
        return operation, data

    def parse_row(self, row):
        operation_key, data = self.parse_operation_and_data(row)
        operation = self.operations_factory.create_operation(operation_key, data)
        return operation

    def parse_stream(self, stream):
        operations = []
        for line in stream:
            try:
                row = line.strip()
                operation = self.parse_row(row)
                operations.append(operation)
            except ValueError as err:
                self.log_error(err)
        return operations

    def log_error(self, err):
        print(f'ERROR: {err}')

    def parse_string(self, table_string):
        stream = io.StringIO(table_string)
        return self.parse_stream(stream)


def main():
    factory = OperationFactory()
    factory.register_operation('sum', SumAggregation)
    factory.register_operation('avg', AverageAggregation)
    factory.register_operation('count', CountAggregation)

    parser = AggregationTableParser(factory)

    table_string = """\
    sum,1,2,3
    avg,1,3,7,1
    sum,a,b,c
    mean,5,5,5
    count,2,2
    avg"""

    operations = parser.parse_string(table_string)
    for operation in operations:
        result = operation.execute()
        print(result)

# Sample Output:
#
# ERROR: could not convert string to float: 'a'
# ERROR: Invalid operation "mean"
# 6.0
# 3.0
# 2
# 0


if __name__ == "__main__":
    main()