# ml-california-housing-price

# Latar Belakang

Dream House Realty Group adalah perusahaan agen real estate yang berfokus pada membantu klien dalam menjual dan menemukan properti impian di California. Dengan tim yang berpengalaman dan pengetahuan yang luas tentang pasar perumahan California, Dream House Realty Group berkomitmen untuk memberikan layanan yang berkualitas dan solusi yang efektif dalam bisnis perumahan.

California memiliki tingkat ekonomi terbesar di negara bagian Amerika Serikat, dan California juga dikenal secara global untuk beberapa hal mulai dari hiburan, relaksasi, hingga bisnis dan ekonomi. Hal-hal tersebut tentu turut andil dalam pertumbuhan bisnis properti di California, di mana banyak orang yang melakukan kegiatan bisnis, pariwisata, investasi, dan lain sebagainya di California dan tentunya membutuhkan properti untuk melangsungkan hidup di California.

Akan tetapi, pada model bisnis yang diterapkan oleh Dream House Realty Group pemilik properti dibebaskan untuk menentukan harga properti yang seringkali berdampak menyulitkan baik dari sisi pemilik maupun pembeli. Jika harganya terlalu mahal dibandingkan dengan properti-properti lain dengan fitur sejenis di sekitar areanya, tentu akan sedikit jumlah calon pembeli yang berminat berpotensi membeli propertinya. Sebaliknya, jika terlalu murah, tentu pemilik tidak akan mendapatkan profit yang sepadan. Banyak faktor yang memengaruhi nilai dari suatu properti. Tentunya hal-hal tersebut perlu dipahami juga oleh pemilik properti karena akan berkaitan dengan profit yang bisa didapatkan.

# Problem Statement

Salah satu tantangan bagi perusahaan Dream House Realty Group adalah pemecahan masalah untuk dapat memiliki model bisnis yang menguntungkan secara finansial bagi pemilik dan pembeli properti. Mengingat Dream House Realty Group memberikan kebebasan kepada pemilik properti untuk menentukan harga properti mereka, pemilik properti dapat memasukkan harga yang lebih tinggi/rendah. Dengan semakin bertambahnya jumlah pemilik dan pembeli properti yang menggunakan jasa Dream House Realty Group, menentukan harga properti yang tepat sangatlah penting.

# Kesimpulan

Dari hasil modelling yang telah dilakukan, didapatkan kesimpulan sebagai berikut : 

- Fitur `median_income` dan `ocean_proximity` menjadi fitur yang paling berpengaruh terhadap `median_house_value`.
- Model yang dipilih adalah `CatBoost Regressor`.
- Ditinjau dari nilai metrics Evaluasi `MAPE` yang telah dihasilkan oleh model sebesar 22%, dapat disimpulkan apabila model digunakan untuk memperkirakan harga properti di California pada rentang nilai sesuai dengan yang dilatih pada model, maka harga yang diprediksi rata-rata dapat meleset kurang lebih sebesar `22%` dari harga aktualnya.

Link Streamlit - Model Deployment :
https://bryanlp27-ml-california-housing-price-app-kzi1le.streamlit.app/
