def truncate(n):
    multiple = 10
    return int(n * multiple) / multiple

def getTotals(Overall_category):
    total = 0
    breakdown = list()
    for category in Overall_category:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(Overall_category):
    result = "Percentage spent by category\n"
    i = 100
    totals = getTotals(Overall_category)
    while i >= 0:
          cat_spaces = " "
          for total in totals:
              if total * 100 >= i:
                  cat_spaces += "o  "
              else:
                  cat_spaces += "   "
          result+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
          i-=10
      
    dashes = "-" + "---"*len(Overall_category)
    names = []
    x_axis = ""
    for n in Overall_category:
          names.append(n.title)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        nameStr = '     '
        for name in names:
              if x >= len(name):
                  nameStr += "   "
              else:
                  nameStr += name[x] + "  "
        
        if(x != len(maxi) -1 ):
          nameStr += '\n'

          
        x_axis += nameStr

    result+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return result

class Category:
  def __init__(self, title):
      self.title = title
      self.ledger = list()

  def __str__(self):
      title = f"{self.title:*^30}\n"
      items = ""
      total = 0
      for n in self.ledger:
          items += f"{n['description'][0:23]:23}" + f"{n['amount']:>7.2f}" + '\n'
          
          total += n['amount']

      output = title + items + "Total: " + str(total)
      return output

  def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})


  def withdraw(self, amount, description=""):
      if(self.check_funds(amount)):
        self.ledger.append({"amount": -amount, "description": description})
        return True
      else :
        return False


  def get_balance(self):
      total_money = 0
      for n in self.ledger:
        total_money += n["amount"]

      return total_money


  def transfer(self, amount, category):
      if(self.check_funds(amount)):
        self.withdraw(amount,"Transfer to " + category.title)
        category.deposit(amount, "Transfer from " + self.title)
        return True
      return False
      

  def check_funds(self, amount):
      if(self.get_balance() >= amount):
        return True
      return False
      
  def get_withdrawls(self):
      total = 0
      for n in self.ledger:
          if n["amount"] < 0:
              total+= n["amount"]
      return total
