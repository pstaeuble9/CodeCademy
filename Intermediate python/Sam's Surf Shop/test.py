# Write your code below:
import surfshop, unittest, datetime

class Testing(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  # old test methods without parametization
  
  # def test_add_surfboards_1(self):
  #   message = self.cart.add_surfboards(quantity=1)
  #   self.assertEqual(message, 'Successfully added 1 surfboard to cart!')

  # def test_add_surfboards_2(self):
  #   message = self.cart.add_surfboards(quantity=2)
  #   self.assertEqual(message, 'Successfully added 2 surfboards to cart!')

    def test_add_surfboards(self):
        for num in range(2, 5):
            with self.subTest(num=num):
                message = self.cart.add_surfboards(num)
                self.assertEqual(message, f'Successfully added {num} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

  @unittest.skip
  def test_too_many_boards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  # error fixed at end of project instructions
  #@unittest.expectedFailure
  def test_apply_local_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)
  
  def test_set_checkout_date(self):
    date = datetime.datetime.now()
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)
    


unittest.main()
