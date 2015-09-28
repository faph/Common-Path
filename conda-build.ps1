Param(
  [switch] $upload = $false
)
$user = 'faph'
$channel = 'dev'

$pyversions = '3.3', '3.4', '3.5'
$build_platform = 'win-64'
$other_platforms = 'osx-64', 'linux-64'

$build_folder = "%LOCALAPPDATA%\Continuum\Miniconda3\conda-bld"

$built_pkgs = @()
foreach ($pyversion in $pyversions) {
    $pkg = conda build conda-recipe --python=$pyversion --output
    $built_pkgs += $pkg
    conda build conda-recipe --python=$pyversion
    if ($lastexitcode -ne 0) {
        Throw "Conda build failed with $lastexitcode"
    }

    $pkg_name = (Get-Item $pkg).Name
    foreach ($platform in $other_platforms) {
        conda convert --platform $platform --output-dir $build_folder $pkg
        if ($lastexitcode -ne 0) {
            Throw "Conda convert failed with $lastexitcode"
        }
        $built_pkgs += "$build_folder\$platform\$pkg_name"
    }
}

if ($upload) {
    foreach ($pkg in $built_pkgs) {
        anaconda upload --user $user --channel $channel --force $pkg
    }
}