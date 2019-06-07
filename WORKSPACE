load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# proto_library, cc_proto_library, and java_proto_library rules implicitly
# depend on @com_google_protobuf for protoc and proto runtimes.
# This statement defines the @com_google_protobuf repo.
git_repository(
    name = "com_google_protobuf",
    commit = "b829ff2a4614ff25048944b2cdc8e43b6488fda0",  # v3.6.1.2
    remote = "https://github.com/protocolbuffers/protobuf.git",
)

# Need to symlink the six repo expected in the protobuf repo.
# This is necessary when loading the py_proto_library rule.
# The version is directly lifted from the protobuf repo WORKSPACE
# at the protobuf repo version listed above.
http_archive(
    name = "six_archive_com_google_protobuf",
    build_file = "@com_google_protobuf//:six.BUILD",
    sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
    urls = ["https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55"],
)

bind(
    name = "six",
    actual = "@six_archive_com_google_protobuf//:six",
)

# Golang build rules. Bazel does not officially support these yet.
git_repository(
    name = "io_bazel_rules_go",
    branch = "master",
    remote = "https://github.com/bazelbuild/rules_go.git",
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains()

# Import build tools for useful QoL stuff.
git_repository(
    name = "com_github_bazelbuild_buildtools",
    commit = "f42fd8fb92a30a55f5e53681975a3d773df8ec7b",  # v0.25.1
    remote = "https://github.com/bazelbuild/buildtools.git",
)

load("@com_github_bazelbuild_buildtools//buildifier:deps.bzl", "buildifier_dependencies")

buildifier_dependencies()

# Python build rules -- while Bazel officially supports Python now, it doesn't
# manage pip dependencies, which is a pain. Let's allow requirements.txt Python
# annotations.
git_repository(
    name = "io_bazel_rules_python",
    branch = "master",  # HEAD
    remote = "https://github.com/bazelbuild/rules_python.git",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_import")

# Python package imports
pip_import(
   name = "requests",
   requirements = "//third_party/py/requests:requirements.txt",
)

load("@requests//:requirements.bzl", "pip_install")

pip_install()
