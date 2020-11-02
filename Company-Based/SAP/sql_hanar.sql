select ord.Orderid from Orders ord
INNER JOIN OrderDetails ords on ords.OrderID = ord.OrderID WHERE ord.CustomerId = "HANAR" order by UnitPrice desc LIMIT 1;