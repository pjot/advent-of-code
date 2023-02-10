import strutils
import sequtils

const WIDTH = 25
const HEIGHT = 6

type
    Layer = seq[int]
    Image = seq[Layer]

proc parse(filename: string): Image =
    let file = readFile filename
    var
        i = 1
        layer: Layer = @[]

    for c in (splitLines file)[0]:
        layer.add (parseInt $c)
        if i == WIDTH * HEIGHT:
            result.add layer
            layer = @[]
            i = 1
        else:
            inc i

func counts(layer: Layer): (int, int, int) =
    var zero, one, two: int
    for i in layer:
        case i
        of 0: inc zero
        of 1: inc one
        of 2: inc two
        else: discard
    return (zero, one, two)

func merge(top, bottom: Layer): Layer =
    for (t, b) in zip(top, bottom):
        if t == 2:
            result.add b
        else:
            result.add t

func decode(image: Image): Layer =
    result = repeat(2, HEIGHT * WIDTH)
    for layer in image:
        result = merge(result, layer)

    return result

proc display(layer: Layer) =
    var line = ""
    for p in layer:
        case p
        of 0: line.add " "
        of 1: line.add "#"
        else: discard

        if len(line) == WIDTH:
            echo line
            line = ""

func check(image: Image): int =
    var fewest = 1000000

    for layer in image:
        let (zeroes, ones, twos) = layer.counts
        if zeroes < fewest:
            fewest = zeroes
            result = ones * twos


let image = parse "image.txt"

echo "Part 1: ", check image
echo "Part 2:"
display(decode image)