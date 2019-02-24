import resource, os, matplotlib.pyplot as plt, matplotlib.animation as animation, numpy as np
from matplotlib.animation import FFMpegWriter
import scipy.ndimage as ndi


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def bw_render(frames, frame_rate, save, fileNameOut):
    f = plt.figure()
    film = []
    for frame in frames:
        film.append([plt.imshow(frame, 'gray')])
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


def bw_labeled_render(frames, frame_rate):
    f = plt.figure()
    film = []
    for frame in frames.values():
        film.append([plt.imshow(frame, 'gray')])
    a = animation.ArtistAnimation(f,film,interval=frame_rate,blit=True,repeat_delay=800)
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


def draw_centered_circle(canvas, radius, value, show):
    cx = canvas.shape[0]/2
    cy = canvas.shape[1]/2
    for x in np.arange(cx - radius, cx + radius, 1):
        for y in np.arange(cy - radius, cy + radius, 1):
            r =np.sqrt((x-cx)*(x-cx) + ((cy-y)*(cy-y)))

            if r <= radius:
                canvas[x, y] = value
    if show:
        plt.imshow(canvas, 'gray_r')
        plt.show()
    return canvas


def draw_centered_box(state, box_sz, value):
    center_x = int(np.array(state).shape[0]/2)
    center_y = int(np.array(state).shape[1] / 2)
    state[center_x-box_sz:center_x+box_sz, center_y-box_sz:center_y+box_sz] = value
    return state


def load_local_images(img_root):
    lib = img_root.decode('hex')
    cmd = "p=$PWD; cd /media; find -name '*.jpg' | cut -b 2- >> $p/pics.txt; cd $p;"
    os.system(cmd)
    pics = swap('pics.txt', True)
    return pics


def labeled_image(imat, title, isBW):
    f = plt.figure()
    if isBW:
        plt.imshow(imat, 'gray')
    else:
        plt.imshow(imat)
    plt.title(title)
    plt.show()


def sharpen(image, factor):
    return ndi.convolve(np.array(image),[[0,0,0],[0,factor,0],[0,0,0]])


def draw_random_points(n_points, initial_state, value):
    state = np.array(initial_state)
    for pt in range(n_points):
        [x,y] = spawn_random_point(state)
        state[x,y] = value
    return state


def draw_rectangle(initial_state, pad, value, show):
    state = initial_state
    padx = pad
    pady = pad
    state[padx, pady:state.shape[1] - pady] = value
    state[padx:state.shape[0] - padx, pady] = value
    state[state.shape[0] - padx, pady:state.shape[1] - pady] = value
    state[pady:state.shape[1] - pady, state.shape[0] - padx] = value

    if show:
        plt.imshow(state, 'gray')
        plt.show()
    return state


def rectangle_accounting(state, pad, value, show):
    box = state[pad:state.shape[0]-pad, pad:state.shape[1]-pad]
    count = 0
    for point in box.flatten():
        if point == value:
            count += 1
    print str(count) + " Matching Values found inside Rectangle"
    return count, box
