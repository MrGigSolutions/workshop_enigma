from revolutionaries.rotor import Rotor


def test_init():
    rotor = Rotor("A'BCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert rotor.rotor_string == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert rotor.connection_string == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert rotor.notched_letters == {"A"}

    rotor = Rotor("A'BCDEFGHIJKLMN'OPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert rotor.rotor_string == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert rotor.connection_string == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert rotor.notched_letters == {"A", "N"}


def test_rotate():
    rotor = Rotor("A'BCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    assert rotor.rotate()
    assert rotor.rotor_string == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    assert rotor.connection_string == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    rotor = Rotor("ZYXWVUTSRQPONMLKJIHGFEDCBA", "TSRQXDZEUNMPHLYVBJIWCAGOFK")

    assert not rotor.rotate()
    assert rotor.rotor_string == "YXWVUTSRQPONMLKJIHGFEDCBAZ"
    assert rotor.connection_string == "RQPWCYDTMLOGKXUAIHVBZFNEJS"


def test_set_rotor_position():
    rotor = Rotor("ABCDEFGHI'JKLMNOPQRSTUVWXYZ", "WJAGOKCPEHLTXFBNIMVUYQZDRS")

    rotor._set_rotor_position(26)

    assert rotor.rotor_string == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert rotor.connection_string == "WJAGOKCPEHLTXFBNIMVUYQZDRS"

    rotor._set_rotor_position(2)

    assert rotor.rotor_string == "CDEFGHIJKLMNOPQRSTUVWXYZAB"
    assert rotor.connection_string == "YEMIANCFJRVDZLGKTSWOXBPQUH"

    rotor = Rotor("ZY'XWVUTSRQPONMLKJIHGFEDCBA", "TSRQXDZEUNMPHLYVBJIWCAGOFK")

    assert rotor._set_rotor_position(2)
    assert rotor.rotor_string == "XWVUTSRQPONMLKJIHGFEDCBAZY"
    assert rotor.connection_string == "POVBXCSLKNFJWTZHGUAYEMDIRQ"


def test_set_position():
    rotor = Rotor("ZY'XWVUTSRQPONMLKJIHGFEDCBA", "TSRQXDZEUNMPHLYVBJIWCAGOFK")

    rotor.set_position("Y")

    assert rotor.rotor_string == "YXWVUTSRQPONMLKJIHGFEDCBAZ"
    assert rotor.connection_string == "RQPWCYDTMLOGKXUAIHVBZFNEJS"

    rotor.set_position("X")

    assert rotor.rotor_string == "XWVUTSRQPONMLKJIHGFEDCBAZY"
    assert rotor.connection_string == "POVBXCSLKNFJWTZHGUAYEMDIRQ"

    rotor.set_position("Y")

    assert rotor.rotor_string == "YXWVUTSRQPONMLKJIHGFEDCBAZ"
    assert rotor.connection_string == "RQPWCYDTMLOGKXUAIHVBZFNEJS"
