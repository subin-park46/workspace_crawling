import folium

my_loc = folium.Map(location=[37.4999072, 127.0373932], zoom_start=18)
folium.Marker([37.4999072, 127.0373932], popup=folium.Popup('멀티캠퍼스 역삼', max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')