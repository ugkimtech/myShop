function addItem(){
    if(document.getElementById("addItem").style.display == 'none'){

        document.getElementById("addItem").style.display = 'block';
        document.getElementById("addStock").style.display = 'none';
        document.getElementById("addSale").style.display = 'none';
        document.getElementById("addExpenditure").style.display = 'none';
    }else{
       document.getElementById("addItem").style.display = 'none';
    }
}

function addStock(){
    if(document.getElementById("addStock").style.display == 'none'){

        document.getElementById("addStock").style.display = 'block';
        document.getElementById("addItem").style.display = 'none';
        document.getElementById("addSale").style.display = 'none';
        document.getElementById("addExpenditure").style.display = 'none';
    }else{
       document.getElementById("addStock").style.display = 'none';
    }
}

function addSale(){
    if(document.getElementById("addSale").style.display == 'none'){

        document.getElementById("addSale").style.display = 'block';
        document.getElementById("addItem").style.display = 'none';
        document.getElementById("addStock").style.display = 'none';
        document.getElementById("addExpenditure").style.display = 'none';
    }else{
       document.getElementById("addSale").style.display = 'none';
    }
}

function addExpenditure(){
    if(document.getElementById("addExpenditure").style.display == 'none'){

        document.getElementById("addExpenditure").style.display = 'block';
        document.getElementById("addItem").style.display = 'none';
        document.getElementById("addStock").style.display = 'none';
        document.getElementById("addSale").style.display = 'none';
    }else{
       document.getElementById("addExpenditure").style.display = 'none';
    }
}

function getStatus(){
    
}