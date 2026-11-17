import os

TEXT = (
    "Late light settles on the field, and the long grass leans in the wind, "
    "each blade bending and rising again in its own time. A river moves past "
    "the stones without hurry, finding its way around them, and the water is "
    "clear enough to see the bottom. Somewhere a thrush calls once, then again, "
    "and the sound has all the room in the world to fade. The air smells of "
    "rain that has already fallen, of earth cooling as the day lets go. There "
    "is nothing to mend here, nothing to reach for. The trees stand where "
    "they have always stood, their branches loose in the evening, and the sky "
    "above them turns the colour of quiet water. There is time to stay a "
    "while. The light will keep its slow work, the grass will keep bending, "
    "and the river will keep going past the stones, unhurried, the way it "
    "always has."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
