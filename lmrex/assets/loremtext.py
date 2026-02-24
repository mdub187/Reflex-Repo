from lmrex.imports import rx


def lorem_image():
	return rx.vstack(
	rx.image(
		src="https://picsum.photos/200",
		width="300px",
		height="300px",
		align_self="center",

	)
)
