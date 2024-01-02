''' THE MATCH with the current score affect the previous score
x: Add the score x
+: Add the sum of 2 previous score
D: Add the score that have the douple value of the previous score
C: Remove the previous score
'''
 
def calPoints(ops) -> int:
        """
        :type ops: List[str] - List of operations
        :rtype: int - Sum of scores after performing all operations
        """
        result = 0
        records = []

        for index in range(len(ops)):
          record_size = len(records)
          print("------- records size: ", record_size)
          value = ops[index]
          print('Value: ', value)
          if value == "+":
            records.append(records[records_size - 1] + records[records_size - 2])
          elif value == "D":
            records.append(2 * records[records_size - 1])
          elif value == "C":
            records.pop(records[records_size - 1])
          else:
            records.append(int(value))
          print('records: ', records)

        for record in records:
          result = result + record
        return result

if __name__ == '__main__':
        print('Please input data. Ex: 5 2 D C +')
        line = input()
        ops = line.strip().split()

        print(calPoints(ops))