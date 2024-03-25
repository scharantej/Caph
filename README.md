### Flask Application Design for Coffee Shop

**Problem:** A coffee shop has three products: coffee, tea, and cake. They want a simple web application to allow customers to order these products online.

**HTML Files**

- `index.html`: The main page of the application, where customers can view the menu and place orders.
- `order.html`: A page that displays the customer's order summary and allows them to confirm their order.

**Routes**

- `/`: Redirects to `index.html`.
- `/menu`: Displays the menu on `index.html`.
- `/order`: Processes an order and redirects to `order.html` with the order summary.
- `/confirm`: Confirms the order and displays a thank-you message.