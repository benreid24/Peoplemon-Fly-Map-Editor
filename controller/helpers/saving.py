import struct

FIELD_TYPE_MAP = {
    'town_count': '=H',
    'disp_name': 'string',
    'ref_name': 'string',
    'map_name': 'string',
    'image': 'string',
    'description': 'string',
    'x': '=H',
    'y': '=H',
    'spawn': '=H'
}


def _pack_field(name, value):
    fmt = FIELD_TYPE_MAP[name]
    if fmt == 'string':
        ret = struct.pack('=I', len(value))
        fmt = '={}s'.format(len(value))
        return ret + struct.pack(fmt, value.encode())
    return struct.pack(fmt, value)


def _unpack_field(name, data, offset):
    fmt = FIELD_TYPE_MAP[name]
    if fmt == 'string':
        length = struct.unpack_from('=I', data, offset)[0]
        offset += 4
        field = struct.unpack_from('={}s'.format(length), data, offset)[0].decode('utf-8')
        offset += length
        return field, offset
    field = struct.unpack_from(fmt, data, offset)[0]
    offset += struct.calcsize(fmt)
    return field, offset


def save_towns(filename, town_list):
    with open(filename, 'wb') as file:
        data = _pack_field('town_count', len(town_list))
        for town in town_list:
            data += _pack_field('x', town['x'])
            data += _pack_field('y', town['y'])
            data += _pack_field('disp_name', town['disp_name'])
            data += _pack_field('ref_name', town['ref_name'])
            data += _pack_field('map_name', town['map_name'])
            data += _pack_field('description', town['description'])
            data += _pack_field('image', town['image'])
            data += _pack_field('spawn', town['spawn'])
        file.write(data)


def load_towns(filename):
    town_list = []
    with open(filename, 'rb') as file:
        data = file.read()
        offset = 0

        town_count, offset = _unpack_field('town_count', data, offset)
        for i in range(0, town_count):
            town = {}
            town['x'], offset = _unpack_field('x', data, offset)
            town['y'], offset = _unpack_field('y', data, offset)
            town['disp_name'], offset = _unpack_field('disp_name', data, offset)
            town['ref_name'], offset = _unpack_field('ref_name', data, offset)
            town['map_name'], offset = _unpack_field('map_name', data, offset)
            town['description'], offset = _unpack_field('description', data, offset)
            town['image'], offset = _unpack_field('image', data, offset)
            town['spawn'], offset = _unpack_field('spawn', data, offset)
            town_list.append(town)

    return town_list
