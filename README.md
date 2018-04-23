# django-indisposable

Disallow disposable email addresses in Django EmailField.

A tiny Django wrapper around https://github.com/FGRibreau/mailchecker. Works with Python 2 and 3.

Denies disposable email addresses with an error message, for example: "*spam4.me email addresses are not accepted.*"

    pip install django-indisposable

## Usage

    import django_indisposable

    # Models:
    email_address = models.EmailField(..., validators=[django_indisposable.validate])

    # Forms:
    email_address = forms.EmailField(..., validators=[django_indisposable.validate])
