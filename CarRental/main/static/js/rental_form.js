// rental_form.js

document.addEventListener('DOMContentLoaded', function () {
    const pickupDatetime = document.getElementById('rental_pickup_Datetime');
    const returnDatetime = document.getElementById('rental_return_Datetime');
    const totalCostSpan = document.getElementById('calculated_total_cost');
  
    // Attach event listeners to calculate total cost on change of pickup or return datetime
    [pickupDatetime, returnDatetime].forEach(function (element) {
      element.addEventListener('change', calculateTotalCost);
    });
  
    function calculateTotalCost() {
      // Implement your logic to calculate the total cost here
      // You can use the values of pickupDatetime.value and returnDatetime.value
      // Update the total cost in the span or div
      totalCostSpan.textContent = 'Calculated Total Cost'; // Replace with your calculated value
    }
  });
  