import fire


def read(infile):
    txt = None
    with open(infile, "r") as f:
        txt = f.read()
    return txt


def write(outfile, output_txt):
    with open(outfile, "w") as f:
        f.write(output_txt)


def cut_out(txt, start_line, stop_line, middle=""):
    lines = txt.split("\n")
    return (
        "\n".join(lines[: start_line - 1])
        + "\n"
        + middle
        + "\n".join(lines[stop_line + 1 :])
    )


def join_lines(t):
    return "\n".join(t)


def find_copy(txt: str):
    lines = txt.split("\n")
    output = {
        "name": "",
        "generics": [],
        "text": "",
    }

    start, stop = None, None
    for i, l in enumerate(lines):
        if "COPY" in l:
            if start is None:
                start = i + 1
                o = l.split(" ")
                output["name"] = o[1]
                output["generics"] = o[2:]
            else:
                stop = i

    output["text"] = join_lines(lines[start:stop])
    cut_txt = cut_out(txt, start, stop)

    return output, cut_txt


def find_and_replace(template: dict[str, str | list[str]], txt: str):
    lines = txt.split("\n")
    start, stop = None, None
    for i, l in enumerate(lines):
        if "PASTE" in l:
            if start is None:
                start = i
            else:
                stop = i

    # replace each name with the given name
    conversions = []  # hold all replacements now
    for i in range(start + 1, stop):
        l = lines[i]
        o = l.strip("\t").split(" ")
        name = o[0]
        args = o[1:]

        s = template["text"]
        for A, B in zip(template["generics"], args):
            s = s.replace(A, B)

        conversions.append(s)

    cut_text = cut_out(txt, start, stop, middle=join_lines(conversions))

    return cut_text


def run(infile, outfile):
    txt = read(infile)
    copy, cut = find_copy(txt)
    out_txt = find_and_replace(copy, cut)
    write(outfile, out_txt)


if __name__ == "__main__":
    # converts .gc to .c file to be compiled and run by the user
    fire.Fire(run)
