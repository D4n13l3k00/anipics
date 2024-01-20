from anipics import AniPics, NekosLife

def main():
    ap = AniPics()
    nl = NekosLife()
    
    print("AniPics:")
    print(ap.get().url)
    
    print("NekosLife:")
    print(nl.get(NekosLife.Types.avatar).url)

if __name__ == "__main__":
    main()