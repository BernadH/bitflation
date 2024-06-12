import bitflation

def tests():
               
  test = bitflation.InflationCalculator(209000)
  test.block_stats(verbose=True)
  test.inflation(starth = 10000, 
               endh = 480000,
               verbose = True,
               type = "harmonized",
               periodicity = "epochly")
  test.inflation(verbose = True,
               type = "price",
               periodicity = "daily")
  test.inflation(type = "cummulative",
               verbose=True)
  test.inflation(starth = 10000,
               verbose = True,
               type = "csnap",
               periodicity = "monthly")
  test.block_stats(block_height=210000)
  test.set_height(210000)
  test.get_supply(verbose=True)
