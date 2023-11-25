def plot_image(image):
    import matplotlib.pyplot as plt
    
    plt.imshow(image, cmap="gray", aspect="equal", 
               extent=[0, image.shape[1], 0, image.shape[0]])
    plt.grid(color="red", linewidth=1)
    plt.xticks(range(0, image.shape[1] + 1))
    plt.yticks(range(0, image.shape[0] + 1))
    plt.tight_layout()
    plt.show()

def plot_channels(channels):
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(1, channels.shape[0])

    for channel, ax, i in zip(channels, axs, range(channels.shape[0])):
        ax.imshow(channel, cmap="gray", aspect="equal", 
                  extent=[0, channel.shape[1], 0, channel.shape[0]])
        ax.grid(color="red", linewidth=1)
        ax.set_title(f"Channel {i}")
        ax.set_xticks(range(0, channel.shape[1] + 1))
        ax.set_yticks(range(0, channel.shape[0] + 1))

    plt.tight_layout()
    plt.show()

