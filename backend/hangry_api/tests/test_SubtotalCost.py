from types import SimpleNamespace

from api.controllers import Subtotal


def test_SimpleCost():
  #Arrange
  order = []
  order.append(SimpleNamespace(quantity=5, item=SimpleNamespace(price=1.0)))
  order.append(SimpleNamespace(quantity=5, item=SimpleNamespace(price=1.0)))
  order.append(SimpleNamespace(quantity=5, item=SimpleNamespace(price=1.0)))
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 15


def test_ComplexCost():
  #Arrange
  order = []
  order.append(SimpleNamespace(quantity=2, item=SimpleNamespace(price=3.5)))
  order.append(SimpleNamespace(quantity=1, item=SimpleNamespace(price=4.5)))
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 11.5
