#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : R-rredlist
Version  : 1.0.0
Release  : 49
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/rredlist_1.0.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/rredlist_1.0.0.tar.gz
Summary  : 'IUCN' Red List Client
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-crul
Requires: R-curl
Requires: R-jsonlite
Requires: R-lifecycle
Requires: R-rlang
BuildRequires : R-cli
BuildRequires : R-crul
BuildRequires : R-curl
BuildRequires : R-jsonlite
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The 'IUCN' Red List is a global list of threatened and endangered species.
    Functions cover all of the Red List 'API' routes. An 'API' key is required.

%prep
%setup -q -n rredlist
pushd ..
cp -a rredlist buildavx2
popd
pushd ..
cp -a rredlist buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738365241

%install
export SOURCE_DATE_EPOCH=1738365241
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rredlist/CITATION
/usr/lib64/R/library/rredlist/DESCRIPTION
/usr/lib64/R/library/rredlist/INDEX
/usr/lib64/R/library/rredlist/LICENSE
/usr/lib64/R/library/rredlist/Meta/Rd.rds
/usr/lib64/R/library/rredlist/Meta/features.rds
/usr/lib64/R/library/rredlist/Meta/hsearch.rds
/usr/lib64/R/library/rredlist/Meta/links.rds
/usr/lib64/R/library/rredlist/Meta/nsInfo.rds
/usr/lib64/R/library/rredlist/Meta/package.rds
/usr/lib64/R/library/rredlist/Meta/vignette.rds
/usr/lib64/R/library/rredlist/NAMESPACE
/usr/lib64/R/library/rredlist/NEWS.md
/usr/lib64/R/library/rredlist/R/rredlist
/usr/lib64/R/library/rredlist/R/rredlist.rdb
/usr/lib64/R/library/rredlist/R/rredlist.rdx
/usr/lib64/R/library/rredlist/WORDLIST
/usr/lib64/R/library/rredlist/doc/benchmarks.Rmd
/usr/lib64/R/library/rredlist/doc/benchmarks.html
/usr/lib64/R/library/rredlist/doc/index.html
/usr/lib64/R/library/rredlist/doc/research_workflows.Rmd
/usr/lib64/R/library/rredlist/doc/research_workflows.html
/usr/lib64/R/library/rredlist/doc/rredlist.Rmd
/usr/lib64/R/library/rredlist/doc/rredlist.html
/usr/lib64/R/library/rredlist/help/AnIndex
/usr/lib64/R/library/rredlist/help/aliases.rds
/usr/lib64/R/library/rredlist/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/rredlist/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/rredlist/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/rredlist/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/rredlist/help/figures/logo.png
/usr/lib64/R/library/rredlist/help/figures/logo.svg
/usr/lib64/R/library/rredlist/help/paths.rds
/usr/lib64/R/library/rredlist/help/rredlist.rdb
/usr/lib64/R/library/rredlist/help/rredlist.rdx
/usr/lib64/R/library/rredlist/html/00Index.html
/usr/lib64/R/library/rredlist/html/R.css
/usr/lib64/R/library/rredlist/tests/fixtures/Rheidae_metadata.yml
/usr/lib64/R/library/rredlist/tests/fixtures/Sturnidae_metadata.yml
/usr/lib64/R/library/rredlist/tests/fixtures/page_assessments_multipage.yml
/usr/lib64/R/library/rredlist/tests/fixtures/page_assessments_singlepage.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_actions-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_actions-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_actions-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_actions.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_actions_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_actions_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_api_version.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_assessment-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_assessment.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_assessment_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_categories-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_categories-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_categories-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_categories.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_categories_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_categories_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_citation.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_class-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_class-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_class-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_class.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_class_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_class_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_comp_groups-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_comp_groups-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_comp_groups-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_comp_groups.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_comp_groups_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_comp_groups_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_countries-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_countries-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_countries-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_countries.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_countries_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_countries_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_extinct-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_extinct.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_extinct_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_extinct_wild-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_extinct_wild.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_extinct_wild_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_family-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_family-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_family-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_family.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_family_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_family_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_faos-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_faos-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_faos-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_faos.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_faos_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_faos_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_green-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_green.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_green_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_growth_forms-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_growth_forms-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_growth_forms-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_growth_forms.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_growth_forms_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_growth_forms_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_habitats-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_habitats-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_habitats-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_habitats.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_habitats_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_habitats_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_kingdom-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_kingdom-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_kingdom-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_kingdom.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_kingdom_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_kingdom_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_order-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_order-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_order-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_order.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_order_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_order_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_phylum-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_phylum-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_phylum-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_phylum.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_phylum_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_phylum_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_pop_trends-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_pop_trends-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_pop_trends-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_pop_trends.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_pop_trends_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_pop_trends_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_realms-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_realms-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_realms-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_realms.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_realms_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_realms_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_research-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_research-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_research-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_research.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_research_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_research_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_scopes-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_scopes-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_scopes-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_scopes.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_scopes_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_scopes_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_sis-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_sis.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_sis_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_sis_latest.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_sp_count.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_sp_count_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_species-badkey.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_species-badquery.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_species-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_species.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_species_-badkey.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_species_-badquery.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_species_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_species_latest.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_stresses-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_stresses-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_stresses-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_stresses.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_stresses_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_stresses_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_systems-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_systems-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_systems-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_systems.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_systems_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_systems_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_threats-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_threats-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_threats-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_threats.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_threats_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_threats_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_threats_no_args.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_threats_with_args.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_use_and_trade-def-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_use_and_trade-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_use_and_trade-not-parsing.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_use_and_trade.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_use_and_trade_-def.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_use_and_trade_.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rl_version.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rr_GET.yml
/usr/lib64/R/library/rredlist/tests/fixtures/rr_GET_raw.yml
/usr/lib64/R/library/rredlist/tests/spelling.R
/usr/lib64/R/library/rredlist/tests/test-all.R
/usr/lib64/R/library/rredlist/tests/testthat/_snaps/rl_categories/scale-color-iucn.svg
/usr/lib64/R/library/rredlist/tests/testthat/_snaps/rl_categories/scale-fill-iucn.svg
/usr/lib64/R/library/rredlist/tests/testthat/helper-rredlist.R
/usr/lib64/R/library/rredlist/tests/testthat/helper-vdiffr.R
/usr/lib64/R/library/rredlist/tests/testthat/test-defunct.R
/usr/lib64/R/library/rredlist/tests/testthat/test-fail-well.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_actions.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_assessment.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_categories.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_citation.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_comp_groups.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_countries.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_extinct.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_extinct_wild.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_faos.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_green.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_growth_forms.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_habitats.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_key.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_latest.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_realms.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_research.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_scopes.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_sis.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_sp_count.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_species.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_stresses.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_systems.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_taxa.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_threats.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_trends.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_use_and_trade.R
/usr/lib64/R/library/rredlist/tests/testthat/test-rl_version.R
/usr/lib64/R/library/rredlist/tests/testthat/test-zzz.R
