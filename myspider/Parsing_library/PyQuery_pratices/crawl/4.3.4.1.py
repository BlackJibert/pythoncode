html = """
<div>
    <ul>
        <li class="item-0 first another"><a href="link1.html"> first item </a> other item<li>
        <li class="item-0 item-1"> <a href="link2.html"> second item </a></li>
        <li class="item-0"> <a href="link3.html"> <span class="bold"> third item </span></a></li>
        <li class="item-0 item-1 active"><a href="link4.html"> fourth item </a></li>
        <li class="item-0"> <a href="link5.html"> fifth item</a></li>
    </ul>
</div>
"""
from pyquery import PyQuery as pq

doc = pq(html)
k = doc('div ul ')
one = k.find('.item-0.first.another').text()
print(one)
