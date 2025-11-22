from .imports import rx


def base_page(*args, **kwargs) -> rx.Component:
	print([type(x) for x in args])

	return rx.container(
		*args,
		**kwargs,

	)
