def get_bio(idioma):
    if idioma == 'eng':
        with open('biography_en.txt') as f:
            bio_txt = f.read()
            return bio_txt

    elif idioma == 'esp':
        with open('biography_es.txt') as f:
            bio_txt = f.read()
            return bio_txt

    else:
        return ValueError('Biography only available in english and spanish (?bio eng OR ?bio esp)\nBiografia solo disponible en ingles y español(?bio esp O ?bio eng)')


def desc_eng():
    desc = "Benjamin Franklin is best known as one of the Founding Fathers who never served as president but was a respected inventor, publisher, scientist and diplomat."
    return desc

def body_eng():
    body = "Benjamin Franklin was a Founding Father and a polymath, inventor, scientist, printer, politician, freemason and diplomat. Franklin helped to draft the Declaration of Independence and the U.S. Constitution, and he negotiated the 1783 Treaty of Paris ending the Revolutionary War. His scientific pursuits included investigations into electricity, mathematics and mapmaking. A writer known for his wit and wisdom, Franklin also published *Poor Richard's Almanack*, invented bifocal glasses and organized the first successful American lending library."
    return body

def desc_esp():
    desc = "Benjamin Franklin es mejor conocido como uno de los padres fundadores que nunca ejercio como presidente, pero fue un inventor, editor, cientifico y diplomatico respetado."
    return desc

def body_esp():
    body = "Benjamin Franklin fue un padre fundador y un polifacetico, inventor, cientifico, impresor, politico, francmason y diplomatico. Franklin ayudo a redactar la Declaracion de Independencia y la Constitucion de los Estados Unidos, y negocio el Tratado de Paris de 1783 que puso fin a la Guerra Revolucionaria. Sus actividades cientificas incluyeron investigaciones sobre electricidad, matematicas y elaboracion de mapas. Un escritor conocido por su ingenio y sabiduria, Franklin tambien publico *Poor Richard's Almanack*, invento las gafas bifocales y organizo la primera biblioteca de prestamos estadounidense con exito."
    return body
