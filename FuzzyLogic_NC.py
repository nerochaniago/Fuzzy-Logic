import csv

true = 0            #variabel untuk menampung nilai layak dalam fungsi inference
false = 0           #variabel untuk menampung nilai tidak layak dalam fungsi inference
penghasilan = []    #array untuk menampung penghasilan
hutang = []         #array untuk menampung hutang
nomor = []          #array untuk menampung nomor
hasil = []          #array untuk menampung hasil
Nchann = []         #array untuk menampung penghasilan dan hutang



with open("DataTugas2.csv","r") as csv_file:
    nc = csv.reader(csv_file)
    next(nc)
    for line in nc:
        nomor.append(int(line[0]))
        penghasilan.append(float(line[1]))
        hutang.append(float(line[2]))


def untukPenghasilan(a):

    global gaji_rendah
    gaji_rendah = 0
    global gaji_tinggi
    gaji_tinggi = 0

    if a >= 0 and  a <= 1.80:
        gaji_rendah = (1.80 - a) / (1.80 - 0 )
        gaji_tinggi = 0
    elif a >= 1.80 and a < 2:
        gaji_rendah = 0
        gaji_tinggi = (a - 1.80) / (2 - 1.80)


def untukHutang(b):

    global hutang_sedikit
    global hutang_banyak
    hutang_sedikit = 0
    hutang_banyak = 0

    if b >= 0 and b <= 35:
        hutang_sedikit = 1
        hutang_banyak = 0
    elif b >= 55 and b < 100:
        hutang_sedikit = 0
        hutang_banyak = 1
    elif b >= 35 and b <= 50:
        hutang_sedikit = (50 - b) / (50 - 35)
        hutang_banyak = 0
    elif b >= 50 and b <= 55:
        hutang_sedikit = 0
        hutang_banyak = (b - 50) / (55 - 50)

def Inference(gaji_rendah, gaji_tinggi, hutang_sedikit, hutang_banyak):

    global true
    global false

    if gaji_rendah > 0 and hutang_sedikit > 0:
        false = min(gaji_rendah,hutang_sedikit)
    elif gaji_tinggi > 0 and hutang_sedikit > 0:
        false = min(gaji_tinggi,hutang_sedikit)
    elif gaji_rendah > 0 and hutang_banyak > 0:
        true = min(gaji_rendah,hutang_banyak)
    elif gaji_tinggi > 0 and hutang_banyak > 0:
        false = min(gaji_tinggi,hutang_banyak)

def Deffuzzyfication(iya,tidak,Nchan):
    nchan = (tidak*30) + (iya*70)
    if nchan > 30:
        hasil.append(Nchann[Nchan][0])

for n in range(0, len(penghasilan) ):
    Nchann.append([nomor[n],penghasilan[n],hutang[n]])

for s in range(0, len(Nchann) ):
    untukPenghasilan(Nchann[s][1])
    untukHutang(Nchann[s][2])
    Inference(gaji_rendah, gaji_tinggi, hutang_sedikit, hutang_banyak)
    Deffuzzyfication(true, false, s)
print(hasil)

with open("TebakanTugas2.csv", 'w') as new_file:
    nech = csv.writer(new_file, delimiter=":")
    for shy in range(0,len(hasil[0:20])):
        nech.writerow(['Keluarga yang Mendapat BLT, Keluarga Nomor  ', hasil[shy]])
