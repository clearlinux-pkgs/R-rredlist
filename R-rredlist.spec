#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rredlist
Version  : 0.5.0
Release  : 14
URL      : https://cran.r-project.org/src/contrib/rredlist_0.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rredlist_0.5.0.tar.gz
Summary  : 'IUCN' Red List Client
Group    : Development/Tools
License  : MIT
Requires: R-base64enc
Requires: R-lazyeval
Requires: R-rlang
BuildRequires : R-base64enc
BuildRequires : R-crul
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-lazyeval
BuildRequires : R-rlang
BuildRequires : R-triebeard
BuildRequires : R-urltools
BuildRequires : R-vcr
BuildRequires : R-withr
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
rredlist
========
[![cran checks](https://cranchecks.info/badges/worst/rredlist)](https://cranchecks.info/pkgs/rredlist)
[![Build Status](https://travis-ci.org/ropensci/rredlist.svg?branch=master)](https://travis-ci.org/ropensci/rredlist)
[![codecov.io](https://codecov.io/github/ropensci/rredlist/coverage.svg?branch=master)](https://codecov.io/github/ropensci/rredlist?branch=master)
[![rstudio mirror downloads](http://cranlogs.r-pkg.org/badges/rredlist)](https://github.com/metacran/cranlogs.app)
[![cran version](http://www.r-pkg.org/badges/version/rredlist)](https://cran.r-project.org/package=rredlist)

%prep
%setup -q -c -n rredlist

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552955130

%install
export SOURCE_DATE_EPOCH=1552955130
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rredlist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rredlist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rredlist
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  rredlist || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rredlist/DESCRIPTION
/usr/lib64/R/library/rredlist/INDEX
/usr/lib64/R/library/rredlist/LICENSE
/usr/lib64/R/library/rredlist/Meta/Rd.rds
/usr/lib64/R/library/rredlist/Meta/features.rds
/usr/lib64/R/library/rredlist/Meta/hsearch.rds
/usr/lib64/R/library/rredlist/Meta/links.rds
/usr/lib64/R/library/rredlist/Meta/nsInfo.rds
/usr/lib64/R/library/rredlist/Meta/package.rds
/usr/lib64/R/library/rredlist/NAMESPACE
/usr/lib64/R/library/rredlist/NEWS.md
/usr/lib64/R/library/rredlist/R/rredlist
/usr/lib64/R/library/rredlist/R/rredlist.rdb
/usr/lib64/R/library/rredlist/R/rredlist.rdx
/usr/lib64/R/library/rredlist/help/AnIndex
/usr/lib64/R/library/rredlist/help/aliases.rds
/usr/lib64/R/library/rredlist/help/paths.rds
/usr/lib64/R/library/rredlist/help/rredlist.rdb
/usr/lib64/R/library/rredlist/help/rredlist.rdx
/usr/lib64/R/library/rredlist/html/00Index.html
/usr/lib64/R/library/rredlist/html/R.css
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_citation.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_common_names-badkey.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_common_names-no-results.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_common_names-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_common_names.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_common_names_-badkey.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_common_names_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_countries-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_countries.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_countries_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_growth_forms-no-results.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_growth_forms-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_growth_forms.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_growth_forms_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_habitats-not-found.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_habitats-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_habitats.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_habitats_-region-not-found.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_habitats_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_history-by-id.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_history-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_history-region-together.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_history.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_history_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_measures-no-results.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_measures-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_measures.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_measures_-region-not-found.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_measures_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_narrative-no-results.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_narrative-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_narrative.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_narrative_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_search-no-results.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_search-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_search.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_search_-region-not-found.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_search_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_sp_category-no-results.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_sp_category-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_sp_category.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_sp_category_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_synonyms-no-results.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_synonyms-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_synonyms.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_synonyms_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_threats-no-results.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_threats-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_threats.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_threats_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/vcr_cassettes/rl_version.yml
/usr/lib64/R/library/rredlist/tests/test-all.R
/usr/lib64/R/library/rredlist/tests/testthat/helper-rredlist.R
/usr/lib64/R/library/rredlist/tests/testthat/test-fail-well.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_citation.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_common_names.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_countries.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_growth_forms.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_habitat.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_history.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_key.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_measures.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_narrative.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_search.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_sp_category.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_synonyms.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_threats.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_version.R
