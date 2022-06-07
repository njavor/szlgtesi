const csrftoken = getCookie('csrftoken');
document.addEventListener('DOMContentLoaded', main);

function main(){

    /// Hiányzók jelölése
    document.querySelectorAll('.apig').forEach(function(gomb){
        gomb.addEventListener('click',async function(){
            fields = this.id.split("-");
            await kuldo_fetch('http://localhost:8000/api/post/jelenlet/',{'a': fields[0], 'd': fields[1], 'vE': fields[2]});
            if(gomb.classList.contains('van')){
                gomb.classList.remove('van');
                gomb.id = fields[0] + "-" + fields[1] + "-nincs";
                gomb.classList.add('nincs');
            }else{
                gomb.classList.remove('nincs');
                gomb.id = fields[0] + "-" + fields[1] + "-van";
                gomb.classList.add('van');
            }
        })
    })
    

    /// Mobil menü
    document.getElementById('hamburger-icon').addEventListener('click', async function(){
        this.classList.toggle("change");
        document.getElementById('mobile-nav').classList.toggle("change");
        document.body.classList.toggle('lock-scroll')
    })
    window.addEventListener('resize', function(){
        hi = document.getElementById('hamburger-icon');
        mn = document.getElementById('mobile-nav');
        if(this.getComputedStyle(hi, null).getPropertyValue("display") === "none"){
            hi.classList.remove("change");
            mn.classList.remove("change");
            document.body.classList.remove('lock-scroll');
        }
    })
}

//////////////////////////////////////
// Fetchek

async function kuldo_fetch(url, szotar){
    const response = await fetch(url, {
        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify(szotar)
    }
    );
    const json_promise = await response.json();
    return json_promise;
}

function getCookie(name) {
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                return decodeURIComponent(cookie.substring(name.length + 1));
            }
        }
    }
    return null;
}