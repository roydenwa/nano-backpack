# src: https://github.com/priya-dwivedi/Deep-Learning/blob/master/depth_estimation/
import matplotlib.pyplot as plt


def get_img_arr(image):
    im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    im = cv2.resize(im, (640, 480))
    x = np.clip(np.asarray(im, dtype=float) / 255, 0, 1)

    return x


def display_single_image(output, inputs=None, is_colormap=True):
    plasma = plt.get_cmap('plasma')
    imgs = []

    imgs.append(inputs)

    # rescale output
    out_min = np.min(output)
    out_max = np.max(output)
    output = output - out_min
    outputs = output/out_max

    if is_colormap:
        rescaled = outputs[:, :, 0]
        pred_x = plasma(rescaled)[:, :, :3]
        imgs.append(pred_x)

    img_set = np.hstack(imgs)

    return img_set
