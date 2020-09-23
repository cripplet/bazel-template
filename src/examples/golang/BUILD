load(
    "@io_bazel_rules_go//go:def.bzl",
    "go_binary",
    "go_library",
    "go_test",
)

go_library(
    name = "app_library",
    srcs = ["app_library.go"],
    importpath = "github.com/minkezhang/bazel-template/srcs/examples/golang",
)

go_test(
    name = "app_test",
    srcs = ["app_test.go"],
    importpath = "github.com/minkezhang/bazel-template/srcs/examples/golang",
    deps = [
        ":app_library",
    ],
)

go_binary(
    name = "app_binary",
    srcs = ["app_binary.go"],
    importpath = "github.com/minkezhang/bazel-template/srcs/examples/golang",
    deps = [
        ":app_library",
    ],
)
