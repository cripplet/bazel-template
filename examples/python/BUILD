py_library(
    name = "app_library",
    srcs = ["app_library.py"],
    deps = [
        "//third_party/py/requests:requests",
    ],
)

py_test(
    name = "app_test",
    srcs = ["app_test.py"],
    deps = [
        ":app_library",
    ],
)

py_binary(
    name = "app_binary",
    srcs = ["app_binary.py"],
    deps = [
        ":app_library",
    ],
)
