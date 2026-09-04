def znajdz_mecze_z_wieloma_golami(lista_goli, prog_goli):
    for gol in lista_goli:
        if gol > prog_goli:
            mecze_z_wieloma_golami.append(gol)
    return mecze_z_wieloma_golami