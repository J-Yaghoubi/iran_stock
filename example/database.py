
import iran_stock as tse

# This example shows how we can update the database
tse.update()

# This example shows how we can read the database
data = tse.check()
print(data)