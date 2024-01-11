#!/usr/bin/python3
"""Lock boxes problem """


def look_next_opened_box(opened):
    """Looks for the next opened box"""
    for i, b in opened.items():
        if b.get('status') == 'opened':
            b['status'] = 'opened/checked'
            return b.get('keys')
    return None


def canUnlockAll(b):
    """Check if all boxes can be opened"""
    if len(b) <= 1 or b == [[]]:
        return True

    a = {}
    while True:
        if len(a) == 0:
            a[0] = {
                'status': 'opened',
                'keys': b[0],
            }
        keys = look_next_opened_box(a)
        if keys:
            for key in keys:
                try:
                    if a.get(key) and a.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    a[key] = {
                        'status': 'opened',
                        'keys': b[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in a.values()]:
            continue
        elif len(a) == len(b):
            break
        else:
            return False

    return len(a) == len(b)


def main():
    """Main function"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
