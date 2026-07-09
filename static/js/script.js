async function updateData(){

    const response = await fetch("/status");

    const data = await response.json();

    document.getElementById("count").innerHTML =
        data.people_count;

    const status =
        document.getElementById("status");

    status.innerHTML =
        data.status;

    if(data.status==="SAFE"){

        status.style.color="green";

    }

    else if(data.status==="MODERATE"){

        status.style.color="orange";

    }

    else{

        status.style.color="red";

    }

}

setInterval(updateData,1000);

updateData();