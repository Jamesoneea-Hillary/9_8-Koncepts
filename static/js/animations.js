const network = document.querySelector(".engineering-network");

if(network){

    const connections = [

        {x1:250,y1:250,x2:120,y2:90},

        {x1:250,y1:250,x2:380,y2:110},

        {x1:250,y1:250,x2:90,y2:250},

        {x1:250,y1:250,x2:410,y2:250},

        {x1:250,y1:250,x2:130,y2:410},

        {x1:250,y1:250,x2:380,y2:390}

    ];

    connections.forEach((line,index)=>{

        const pulse=document.createElement("div");

        pulse.className="energy-pulse";

        network.appendChild(pulse);

        let progress=Math.random();

        function animate(){

            progress+=0.003;

            if(progress>1){

                progress=0;

            }

            const x=line.x1+(line.x2-line.x1)*progress;

            const y=line.y1+(line.y2-line.y1)*progress;

            pulse.style.left=x+"px";

            pulse.style.top=y+"px";

            requestAnimationFrame(animate);

        }

        setTimeout(animate,index*400);

    });

}