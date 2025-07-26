import imageio.v3 as iio

iio.imwrite(
    'team.gif',
    [iio.imread(f) for f in ['team-pic1.png', 'team-pic2.png']],
    duration=500,
    loop=0
)
