$("#user-tab").click(function () {
    document.getElementById("list-your-items").style.display="block";
    document.getElementById("view-listed-products").style.display="none";
  });
  $("#product-tab").click(function () {
    document.getElementById("list-your-items").style.display="none";
    document.getElementById("view-listed-products").style.display="block";
  });