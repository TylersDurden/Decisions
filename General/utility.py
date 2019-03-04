from matplotlib.animation import FFMpegWriter
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import freetype as ft
import numpy as np
import resource


def show(matrix, name, isColor):
    f = plt.figure()
    if isColor:
        plt.imshow(matrix)
    else:
        plt.imshow(matrix, 'gray')
    plt.title(name)
    plt.show()


def bw_render(frames, frame_rate, save, fileNameOut):
    f = plt.figure()
    film = []
    for frame in frames:
        film.append([plt.imshow(frame, 'gray_r')])
    a = animation.ArtistAnimation(f, film, interval=frame_rate, blit=True, repeat_delay=900)
    if save:
        writer = FFMpegWriter(fps=frame_rate, metadata=dict(artist='Me'), bitrate=1800)
        a.save(fileNameOut, writer=writer)
    plt.show()


def color_render(frames, frame_rate, save, fileNameOut):
    f = plt.figure()
    film = []
    for frame in frames:
        film.append([plt.imshow(frame, 'rainbow')])
    a = animation.ArtistAnimation(f, film, interval=frame_rate, blit=True, repeat_delay=900)
    if save:
        writer = FFMpegWriter(fps=frame_rate, metadata=dict(artist='Me'), bitrate=1800)
        a.save(fileNameOut, writer=writer)
    plt.show()


def check_mem_usage():
    """
    Return the amount of RAM usage, in bytes, being consumed currently.
    :return (integer) memory:
    """
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return mem


def filter_preview(images):
    f, ax = plt.subplots(1, len(images.keys()))
    II = 0
    for image in images.keys():
        ax[II].imshow(images[image], 'gray_r')
        ax[II].set_title(image)
        II += 1
    plt.show()


def ind2sub(index,dims):
    """
    Given an index and array dimensions,
    convert an index to [x,y] subscript pair.
    :param index:
    :param dims:
    :return tuple - subscripts :
    """
    subs = []
    ii = 0
    for y in range(dims[1]):
        for x in range(dims[0]):
            if index==ii:
                subs = [x,y]
            ii +=1
    return subs


def sub2ind(subs, dims):
    """
    Given a 2D Array's subscripts, return it's
    flattened index
    :param subs:
    :param dims:
    :return:
    """
    ii = 0
    indice = 0
    for y in range(dims[1]):
        for x in range(dims[0]):
            if subs[0] == x and subs[1] == y:
                indice = ii
            ii += 1
    return indice


def spawn_random_point(state):
    # Initialize a random position
    x = np.random.randint(0, state.shape[0], 1, dtype=int)
    y = np.random.randint(0, state.shape[1], 1, dtype=int)
    return [x, y]


def draw_centered_circle(canvas, radius, show):
    cx = canvas.shape[0]/2
    cy = canvas.shape[1]/2
    for x in np.arange(cx - radius, cx + radius, 1):
        for y in np.arange(cy - radius, cy + radius, 1):
            r =np.sqrt((x-cx)*(x-cx) + ((cy-y)*(cy-y)))

            if r <= radius:
                canvas[x, y] = 1
    if show:
        plt.imshow(canvas, 'gray_r')
        plt.show()
    return canvas


def create_point_cloud(state_size, cloud_size, n_points, show):
    asize = cloud_size
    bsize = state_size
    pad = (bsize - asize) / 2
    blob = np.zeros((asize, asize))
    points = {}
    ii = 0
    for i in range(n_points):
        point = spawn_random_point(np.zeros((asize, asize)))
        r = np.sqrt(((point[0] - pad) * (point[0] - pad) + (point[1] - pad) * (point[1] - pad)))
        if r <= (asize - pad):
            blob[point[0], point[1]] = 1
            points[ii] = point
        ii += 1
    cloud = np.zeros((bsize, bsize))
    cloud[pad:bsize-pad, pad:bsize-pad] = blob
    # Show the cloud if flagged
    if show:
        plt.imshow(cloud, 'gray')
        plt.show()
    return cloud, points


def create_font_mappings():
    alpha = ['a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x',
             'y', 'z']

    specials = [' ', ',', '.', '!', '?',
                ':', ';', '/', '>', '<']  # TODO: Add more

    mappings = {}
    for letter in alpha:
        tface = ft.Face('/snap/wine-platform/58/opt/wine-staging/share/wine/fonts/arial.ttf')
        tface.set_char_size(48 * 64)
        tface.load_char(letter)
        bitmap = tface.glyph.bitmap
        mappings[letter] = np.array(bitmap.buffer).reshape(bitmap.rows, bitmap.width)
    for letter in alpha:
        tface = ft.Face('/snap/wine-platform/58/opt/wine-staging/share/wine/fonts/arial.ttf')
        tface.set_char_size(48 * 64)
        tface.load_char(letter.upper())
        bitmap = tface.glyph.bitmap
        mappings[letter.upper()] = np.array(bitmap.buffer).reshape(bitmap.rows, bitmap.width)
    for character in specials:
        tface = ft.Face('/snap/wine-platform/58/opt/wine-staging/share/wine/fonts/arial.ttf')
        tface.set_char_size(48 * 64)
        tface.load_char(character)
        bitmap = tface.glyph.bitmap
        mappings[character] = np.array(bitmap.buffer).reshape(bitmap.rows, bitmap.width)
    print str(len(mappings.keys())) + " Characters Mapped to Font Imagery"
    return mappings


def draw_text(text, mapping, show):
    pad = mapping['A'].shape
    n_letters = len(list(text))
    state = np.zeros((n_letters*pad[0], n_letters*pad[1]))
    print state.shape
    x = 0
    for letter in list(text):
        font_let = mapping[letter]
        sz = font_let.shape
        state[0:sz[0],x:x+sz[1]] = font_let
        x += sz[1]+1
        # TODO: Allign letters properly
    if show:
        plt.imshow(state, 'gray')
        plt.show()
    return state

