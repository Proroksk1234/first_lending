window.onload=function(){
    const navigate = document.querySelector('.navigate-body')
    const lineParent = document.querySelector('[data-line-parent]')
    const lineItems = document.querySelectorAll('[data-line-item]')
    const lineBlocks  =document.querySelectorAll('[data-line-block]')
    if(lineParent){
        lineParent.insertAdjacentHTML(
            'beforeend',
            '<div class="line"></div>'
        )
    }
    const lineStyle =getComputedStyle(document.querySelector('.line'))
    const lineTransition = lineStyle.transition
    function setValues(target, hide){
        const line = target.closest('[data-line-parent]').querySelector('.line')
        if(!hide){
            const width = target.getBoundingClientRect().width
            const leftItem = target.getBoundingClientRect().left
            const bottomItem = target.getBoundingClientRect().bottom
            const leftParent = target.closest('[data-line-parent]').getBoundingClientRect().left
            const bottomParent = target.closest('[data-line-parent]').getBoundingClientRect().bottom
            const left = leftItem - leftParent
            const bottom = bottomParent - bottomItem
            line.style.width = `${width}px`
            line.style.bottom = `${bottom}px`
            line.style.left = `${left}px`
        }
        else{
            line.style.width='0'
        }
    }
    function mouseenterFunc(){
        setValues(this)
    }
    function mouseleaveFunc(){
        const lineItemActive= document.querySelector("[data-line-item]._active")
        if(lineItemActive){
            setValues(lineItemActive)
        }
        else{
            setValues(this,true)
        }
    }
    function resizeFunc(){
        const lineItemActive = document.querySelector('[data-line-item]._active')
        if(lineItemActive){
            const line = lineItemActive.closest('[data-line-parent]').querySelector('.line')
            line.style.transition='none'
            setValues(lineItemActive)
            line.style.transition=lineTransition
        }
    }
    function clickFunc(e){
        if(e.target.closest('[data-line-item]')){
            const lineItemValue = e.target.closest('[data-line-item]').getAttribute('data-line-item')
            if(lineItemValue){
                const blockScrollTo = document.querySelector(`[data-line-block="${lineItemValue}"]`)
                const lineItemActive = document.querySelector('[data-line-item]._active')
                lineBlocks.forEach(lineBlock=>{
                    observer.unobserve(lineBlock)
                })
                if(lineItemActive){
                    lineItemActive.classList.remove('_active')
                }
                e.target.closest('[data-line-item]').classList.add('_active')
                if(blockScrollTo){
                    const blockScrollToTop=blockScrollTo.getBoundingClientRect().top+pageYOffset
                    window.scrollTo({
                        top: blockScrollToTop,
                        behavior: "smooth"
                    })
                }
                setTimeout(() => {
                    lineBlocks.forEach(lineBlock=>{
                        observer.observe(lineBlock)
                    })
                }, 1);
            }
        }
    }
    document.addEventListener('click',clickFunc);
    window.addEventListener('resize',resizeFunc);
    lineItems.forEach(lineItem => {
        lineItem.addEventListener('mouseenter', mouseenterFunc)
        lineItem.addEventListener('mouseleave',mouseleaveFunc)
    })
    const changeLineItem = (entries, observer)=>{
        entries.forEach(entry=>{
            if(entry.isIntersecting){
                const blockVisible = entry.target.getAttribute('data-line-block')
                const lineItemVisible = document.querySelector(`[data-line-item="${blockVisible}"]`)
                if(lineItemVisible){
                    lineItemVisible.classList.add('_active')
                    setTimeout(() => {
                        setValues(lineItemVisible)
                    }, 1 )
                }
            }
            else{
                const blockVisible = entry.target.getAttribute('data-line-block')
                const lineItemVisible = document.querySelector(`[data-line-item="${blockVisible}"]`)
                if(lineItemVisible){
                    lineItemVisible.classList.remove('_active')
                    setValues(lineItemVisible, true)
                }
            }
        })
    }
    const options ={
        threshold:0.5
    }
    const observer = new IntersectionObserver(changeLineItem, options)
    lineBlocks.forEach(lineBlock=>{
        observer.observe(lineBlock)
    })
}

const addOrderButton = document.querySelector('.button-add-service')
const closeWindow =document.querySelector('.close')
const addOrderWindow =document.querySelector('.add-order')
const addOrderWindowHide = ()=>{
    addOrderWindow.style.display='none'
}
const addOrderWindowShow = ()=>{
    if(window.screen.height<=400){
        addOrderWindow.style.display='flex'
    }
    else{
        addOrderWindow.style.display='block'
    }
}

addOrderButton.addEventListener('click',addOrderWindowShow)
closeWindow.addEventListener('click',addOrderWindowHide)
document.querySelector('.c-hamburger').addEventListener('click',function(e){
    e.preventDefault()
    if(this.classList.contains('is-active')){
        this.classList.remove('is-active')
        document.querySelector('#menu').classList.remove('nav-active')
        document.body.classList.remove('body-active')
    }
    else{
        this.classList.add('is-active')
        document.querySelector('#menu').classList.add('nav-active')
        document.body.classList.add('body-active')
    }
})
const anchors = document.querySelectorAll('a[href*="#"]')
for(let anchor of anchors){
    anchor.addEventListener("click",function(event){
        event.preventDefault()
        const blockId = anchor.getAttribute('href')
        document.querySelector(''+blockId).scrollIntoView({
            behavior: "smooth",
            block:"start"
        })
    })
}