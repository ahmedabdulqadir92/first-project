/*1 Select customer name together with each order the customer made*/
select c.CustomerName,o.OrderID 
from customers c 
inner join orders o 
on c.CustomerID=o.CustomerID;

/*2 Select order id together with name of employee who handled the order*/

select o.OrderID,e.FirstName
from employees e
inner join orders o 
on o.EmployeeID=e.EmployeeID;

/*3 Select customers who did not placed any order yet*/
select * 
from customers c left join orders o 
on c.CustomerID=o.CustomerID
where o.OrderID is null;

/*4 Select order id together with the name of products*/
select p.ProductName,count(od.OrderID) as numberofsales
from order_details od 
inner join products p 
on p.ProductID=od.ProductID
group by p.ProductName
order by numberofsales desc
limit 5;

/*5 Select products that no one bought*/

select * 
from  products p left join order_details od
on od.ProductID=p.ProductID
where od.OrderDetailID is null;




/*6. Select customer together with the products that he bought*/
select c.CustomerName,p.ProductName,p.Price
from customers c 
inner join orders o 
on c.CustomerID=o.CustomerID
inner join order_details od 
on o.OrderID=od.OrderID
inner join products p 
on od.ProductID=p.ProductID;


/*7. Select product names together with the name of corresponding category*/


/*8. Select orders together with the name of the shipping company*/


/*9. Select customers with id greater than 50 together with each order they made*/


/*10. Select employees together with orders with order id greater than 10400*/


#11 Select orderID together with the total price of  that Order, order the result by total price of order in increasing order*/


#12. Select customer who spend the most money


#13. Select customer who spend the most money and lives in Canada


#14. Select customer who spend the second most money


#15. Select shipper together with the total price of proceed orders


/*16. Select name of the cheapest product (only name) using subquery*/
