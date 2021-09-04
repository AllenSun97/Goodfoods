var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var dishId = this.dataset.dish
        var action = this.dataset.action
        console.log('dishId:',dishId, 'action',action)

        console.log('USER:',user)
        if (user == 'AnonymousUser'){
            console.log('Not logged in')
            alert('Login to purchase')
            window.location.href = "{% url 'login' %}"
        }else{
            updateUserOrder(dishId, action)
        }
    })
};

function updateUserOrder(dishId, action){
    console.log('User is logged in, sending data...')

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'dishId':dishId, 'action':action})
    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        console.log('data:',data)
        location.reload()
    })
}