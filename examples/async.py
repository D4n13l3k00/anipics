from anipics import AniPics, NekosLife
import asyncio

async def main():
    ap = AniPics()
    nl = NekosLife()
    
    print("AniPics:")
    print((await ap.async_get()).url)
    
    print("NekosLife:")
    print((await nl.async_get(NekosLife.Types.avatar)).url)

if __name__ == "__main__":
    asyncio.run(main())