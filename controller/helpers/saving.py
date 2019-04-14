import struct

FIELD_TYPE_MAP = {
    'song': 'string',
    'song_count': '=H',
}


def _pack_field(name, value):
    fmt = FIELD_TYPE_MAP[name]
    if fmt == 'string':
        ret = struct.pack('=I', len(value))
        fmt = '={}s'.format(len(value))
        return ret + struct.pack(fmt, value.encode())
    return struct.pack(fmt, value)


def save_towns(filename, song_list):
    with open(filename, 'wb') as file:
        data = _pack_field('song_count', len(song_list))
        for song in song_list:
            data += _pack_field('song', song)
        file.write(data)


def load_towns(filename):
    song_list = []
    with open(filename, 'rb') as file:
        data = file.read()
        offset = 0

        song_count = struct.unpack_from('=H', data, offset)[0]
        offset += 2
        for i in range(0, song_count):
            length = struct.unpack_from('=I', data, offset)[0]
            offset += 4
            song = struct.unpack_from('={}s'.format(length), data, offset)
            offset += length
            song_list.append(song)

    return song_list
