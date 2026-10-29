#trascrição de tudo para segundos 

def seg(h, m, s):

    seg_hora = h * 3600
    seg_min = m * 60
    segundos = seg_hora + seg_min + s

    return segundos

# trasnformação dos segundos em hora, minuto e segundo novamente

def hms(segs):
    hr = segs // 3600
    mnt = (segs // 60) % 60
    sg = segs % 60
    print(f'diferenca em s: {segs} = {hr} horas, {mnt}min e {sg}s')

def main():

    h1 = int(input('horas: '))
    m1 = int(input('minutos: '))
    s1 = int(input('segundos: '))

    h2 = int(input('horas: '))
    m2 = int(input('minutos: '))
    s2 = int(input('segundos: '))

    conversao1_seg = seg(h1, m1, s1)
    conversao2_seg = seg(h2, m2, s2)

    #encontrando a conversão que resulta num valor maior
    if conversao1_seg > conversao2_seg:
        diferenca = conversao1_seg - conversao2_seg
    else:
        diferenca = conversao2_seg - conversao1_seg
    
    hms(diferenca)

main()