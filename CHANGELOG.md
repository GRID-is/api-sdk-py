# Changelog

## 1.9.0 (2025-11-18)

Full Changelog: [v1.8.2...v1.9.0](https://github.com/GRID-is/api-sdk-py/compare/v1.8.2...v1.9.0)

### Features

* **api:** api update ([1fa7527](https://github.com/GRID-is/api-sdk-py/commit/1fa752707eb9544e405847003849ae89930b6779))
* **api:** api update ([7fec694](https://github.com/GRID-is/api-sdk-py/commit/7fec69437520ff1fc08583df288d319150d0f48d))


### Bug Fixes

* compat with Python 3.14 ([bf3e37a](https://github.com/GRID-is/api-sdk-py/commit/bf3e37a063d9476179b244fd24c6234366420bae))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([43cb15d](https://github.com/GRID-is/api-sdk-py/commit/43cb15dc4f97a8b4ab20ac930092d8bfe0756fe4))


### Chores

* **package:** drop Python 3.8 support ([1629ff2](https://github.com/GRID-is/api-sdk-py/commit/1629ff2e7ecf1722a847f2f91a5405a50918e9e6))

## 1.8.2 (2025-11-04)

Full Changelog: [v1.8.1...v1.8.2](https://github.com/GRID-is/api-sdk-py/compare/v1.8.1...v1.8.2)

### Bug Fixes

* **client:** close streams without requiring full consumption ([8906ad6](https://github.com/GRID-is/api-sdk-py/commit/8906ad6b2eb942ceec099ddb19040ef73fd8288d))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([fb5ad9f](https://github.com/GRID-is/api-sdk-py/commit/fb5ad9fc4c21ce76d2d78a59ae1e485ce7f15a37))
* **internal/tests:** avoid race condition with implicit client cleanup ([27e2ad9](https://github.com/GRID-is/api-sdk-py/commit/27e2ad987e5ba355f7690df185b061a478c70e20))
* **internal:** detect missing future annotations with ruff ([f9403b6](https://github.com/GRID-is/api-sdk-py/commit/f9403b6252a4110eb83881bc3b59c61920289823))
* **internal:** grammar fix (it's -&gt; its) ([2f19622](https://github.com/GRID-is/api-sdk-py/commit/2f19622fcb12ee76a137a4a67924f233204d0343))

## 1.8.1 (2025-09-20)

Full Changelog: [v1.8.0...v1.8.1](https://github.com/GRID-is/api-sdk-py/compare/v1.8.0...v1.8.1)

### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([fc64cf4](https://github.com/GRID-is/api-sdk-py/commit/fc64cf4ec5226af7dd31e9c61f59a5b15bbfa70b))
* **internal:** update pydantic dependency ([96eb756](https://github.com/GRID-is/api-sdk-py/commit/96eb756ef7c3b163b0102af73fb1129bb23a2fc0))
* **types:** change optional parameter type from NotGiven to Omit ([65042e5](https://github.com/GRID-is/api-sdk-py/commit/65042e58c76c40160e3a24cf3c213b67f8c6463d))

## 1.8.0 (2025-09-15)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/GRID-is/api-sdk-py/compare/v1.7.0...v1.8.0)

### Features

* improve future compat with pydantic v3 ([0a08691](https://github.com/GRID-is/api-sdk-py/commit/0a08691df0dda690a0bd2482e5236463b527c202))
* **types:** replace List[str] with SequenceNotStr in params ([0b48994](https://github.com/GRID-is/api-sdk-py/commit/0b48994c1676d71d1d69a7b6d05ca9aa57ca846f))


### Bug Fixes

* avoid newer type syntax ([02b4ff1](https://github.com/GRID-is/api-sdk-py/commit/02b4ff1604bf3ee57b386ad207ccc0b35e438349))


### Chores

* **internal:** add Sequence related utils ([ee8f98e](https://github.com/GRID-is/api-sdk-py/commit/ee8f98e356eb7a936f1b9d1903031075289d63a8))
* **internal:** change ci workflow machines ([883586d](https://github.com/GRID-is/api-sdk-py/commit/883586d1d2a902a7c02430bea0eead580fb6309c))
* **internal:** move mypy configurations to `pyproject.toml` file ([c8be74c](https://github.com/GRID-is/api-sdk-py/commit/c8be74c073cd5466efd708e83c8a3220a6ef075f))
* **internal:** update pyright exclude list ([df56c6f](https://github.com/GRID-is/api-sdk-py/commit/df56c6f85d691b66dc816e849ebaeb6f2ca9e65e))
* **tests:** simplify `get_platform` test ([1838149](https://github.com/GRID-is/api-sdk-py/commit/1838149ff9f7b7500d73a88deffcb818048bb9e9))
* update github action ([8d15170](https://github.com/GRID-is/api-sdk-py/commit/8d15170470775c8c23ac7ddeb91ab29ebaa2851b))

## 1.7.0 (2025-08-20)

Full Changelog: [v1.6.1...v1.7.0](https://github.com/GRID-is/api-sdk-py/compare/v1.6.1...v1.7.0)

### Features

* **api:** api update ([af9f3b9](https://github.com/GRID-is/api-sdk-py/commit/af9f3b9d6a556706f4809aa2926d01f0928ef0aa))

## 1.6.1 (2025-08-20)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/GRID-is/api-sdk-py/compare/v1.6.0...v1.6.1)

### Features

* **api:** api update ([c43ac66](https://github.com/GRID-is/api-sdk-py/commit/c43ac6630a321bc500af2cdfee85f1ca8d711bae))

## 1.6.0 (2025-08-20)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/GRID-is/api-sdk-py/compare/v1.5.0...v1.6.0)

### Features

* **api:** api update ([962357d](https://github.com/GRID-is/api-sdk-py/commit/962357d4977c51c98ec17341a2c4a6470037051d))


### Chores

* **internal:** codegen related update ([7ab56d8](https://github.com/GRID-is/api-sdk-py/commit/7ab56d823a39320b1eb52fd38f07b2745017c513))
* **internal:** fix ruff target version ([3f18ec2](https://github.com/GRID-is/api-sdk-py/commit/3f18ec2df732ba83dfae6038a1b4aa765df81d6f))
* **internal:** update comment in script ([b3b3b52](https://github.com/GRID-is/api-sdk-py/commit/b3b3b52edd1883551c957ffcf5d2b961bd0c6a84))
* update @stainless-api/prism-cli to v5.15.0 ([181e638](https://github.com/GRID-is/api-sdk-py/commit/181e6382154c2ed67bc19c55ed2849670399ebbe))

## 1.5.0 (2025-07-31)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/GRID-is/api-sdk-py/compare/v1.4.0...v1.5.0)

### Features

* **client:** support file upload requests ([d397e17](https://github.com/GRID-is/api-sdk-py/commit/d397e17f77364bc32e218fb1150c8025c64142a8))


### Bug Fixes

* **parsing:** ignore empty metadata ([06f7815](https://github.com/GRID-is/api-sdk-py/commit/06f78159f245ba0f507a72938b043f55f21158b5))
* **parsing:** parse extra field types ([d775cee](https://github.com/GRID-is/api-sdk-py/commit/d775cee17b1229ac3cf2325dff248ea8c668c876))


### Chores

* **project:** add settings file for vscode ([ed9fc24](https://github.com/GRID-is/api-sdk-py/commit/ed9fc246ccb026f04f45111c4ae53ad8ec4bc62f))

## 1.4.0 (2025-07-15)

Full Changelog: [v1.3.1...v1.4.0](https://github.com/GRID-is/api-sdk-py/compare/v1.3.1...v1.4.0)

### Features

* clean up environment call outs ([e567d38](https://github.com/GRID-is/api-sdk-py/commit/e567d383cde39c8f3df3facaea75d03f4c77b820))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([e83a775](https://github.com/GRID-is/api-sdk-py/commit/e83a77545f0d2b9f651381cc53c72b9605a28cc7))
* **parsing:** correctly handle nested discriminated unions ([ba4c542](https://github.com/GRID-is/api-sdk-py/commit/ba4c54231aa508bc637824cb3db0ebb6d7d35cce))


### Chores

* **ci:** change upload type ([88d4f3f](https://github.com/GRID-is/api-sdk-py/commit/88d4f3fdf939fc2f87683126bcf5cdf3f4a6498c))
* **internal:** bump pinned h11 dep ([174da39](https://github.com/GRID-is/api-sdk-py/commit/174da393ffaeab03f17ad8961a43e7b9ee992715))
* **internal:** codegen related update ([0232dae](https://github.com/GRID-is/api-sdk-py/commit/0232daefd3235ce165d796c07b0219e38bd999d8))
* **package:** mark python 3.13 as supported ([efd6017](https://github.com/GRID-is/api-sdk-py/commit/efd60178d934283acba6db07a95b8ff1cf022cf9))
* **readme:** fix version rendering on pypi ([71c5198](https://github.com/GRID-is/api-sdk-py/commit/71c51980028d935e77a3fc2655abad2f422efe3d))

## 1.3.1 (2025-06-30)

Full Changelog: [v1.3.0...v1.3.1](https://github.com/GRID-is/api-sdk-py/compare/v1.3.0...v1.3.1)

### Bug Fixes

* **ci:** correct conditional ([ec7ad05](https://github.com/GRID-is/api-sdk-py/commit/ec7ad0559078ba69197953e7f33f652c283d6dff))
* **ci:** release-doctor — report correct token name ([28e054f](https://github.com/GRID-is/api-sdk-py/commit/28e054f80e4a71a641737ce2f8886e079adad438))


### Chores

* **ci:** only run for pushes and fork pull requests ([db922e2](https://github.com/GRID-is/api-sdk-py/commit/db922e2f05204059277d34878637a5f50bb4c8de))
* **tests:** skip some failing tests on the latest python versions ([7449172](https://github.com/GRID-is/api-sdk-py/commit/7449172d1aa289cd6c02340eb2f4453584beb3ce))

## 1.3.0 (2025-06-21)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/GRID-is/api-sdk-py/compare/v1.2.0...v1.3.0)

### Features

* **client:** add support for aiohttp ([a9b8ed3](https://github.com/GRID-is/api-sdk-py/commit/a9b8ed3beb44e46e181cbe49912655f13be0c903))


### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([9a58f1f](https://github.com/GRID-is/api-sdk-py/commit/9a58f1fe5ef22f3fc6a7845e00cf3ca4afabf2b7))


### Chores

* **ci:** enable for pull requests ([b236e91](https://github.com/GRID-is/api-sdk-py/commit/b236e918c09758eaf3e7c578d9274867112ccb95))
* **internal:** update conftest.py ([ccb4ee4](https://github.com/GRID-is/api-sdk-py/commit/ccb4ee4378e63e421ee1c2998e183ff027afcc8f))
* **readme:** update badges ([725de9c](https://github.com/GRID-is/api-sdk-py/commit/725de9c4df16aab6e736aee65ec22b38b79e1d30))
* **tests:** add tests for httpx client instantiation & proxies ([b4d8d52](https://github.com/GRID-is/api-sdk-py/commit/b4d8d5221fce1958f633eea12c6e52598c3f47fd))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([b3d9d93](https://github.com/GRID-is/api-sdk-py/commit/b3d9d934f291fe805dc2ceef6a5e29cd2c50581f))

## 1.2.0 (2025-06-13)

Full Changelog: [v1.1.2...v1.2.0](https://github.com/GRID-is/api-sdk-py/compare/v1.1.2...v1.2.0)

### Features

* **client:** add follow_redirects request option ([7154df6](https://github.com/GRID-is/api-sdk-py/commit/7154df67405d7c130cd27127aaf77fc3b912380a))


### Bug Fixes

* **client:** correctly parse binary response | stream ([ece61b6](https://github.com/GRID-is/api-sdk-py/commit/ece61b6af6c41164d1dd40b26008a49130d85785))


### Chores

* **docs:** remove reference to rye shell ([6dc6cf1](https://github.com/GRID-is/api-sdk-py/commit/6dc6cf11fd3f887cc0069dc40cc916304e1f60e9))
* **internal:** codegen related update ([9093fc0](https://github.com/GRID-is/api-sdk-py/commit/9093fc03f4f579fae4da1177502ab461015826a9))
* **tests:** run tests in parallel ([7b9550c](https://github.com/GRID-is/api-sdk-py/commit/7b9550c9f70e5b91f7b874b89a159445aadf7e2a))

## 1.1.2 (2025-05-27)

Full Changelog: [v1.1.1...v1.1.2](https://github.com/GRID-is/api-sdk-py/compare/v1.1.1...v1.1.2)

### Features

* **api:** api update ([8e0e977](https://github.com/GRID-is/api-sdk-py/commit/8e0e977d728d2d479a1207a61e13590154a049f4))
* **api:** api update ([9f6051e](https://github.com/GRID-is/api-sdk-py/commit/9f6051e57e933c42c651d9ecd92ff2e5b41476e4))

## 1.1.1 (2025-05-23)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/GRID-is/api-sdk-py/compare/v1.1.0...v1.1.1)

### Bug Fixes

* **api:** Add label parameters endpoint ([6f784a5](https://github.com/GRID-is/api-sdk-py/commit/6f784a53a783d60a7137060a8ad9c96e05a47d17))

## 1.1.0 (2025-05-23)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/GRID-is/api-sdk-py/compare/v1.0.1...v1.1.0)

### Features

* **api:** add beta label endpoints ([c24387c](https://github.com/GRID-is/api-sdk-py/commit/c24387c8b4179c1faa69811ba35389fbf09d3446))


### Chores

* **ci:** fix installation instructions ([8d1ae96](https://github.com/GRID-is/api-sdk-py/commit/8d1ae96853d64a373bb089d3ab98b18b57259e95))
* **docs:** grammar improvements ([fcb3bf4](https://github.com/GRID-is/api-sdk-py/commit/fcb3bf46caa1a95d76f971359a73b6a867f88bee))

## 1.0.1 (2025-05-15)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0...v1.0.1)

### Bug Fixes

* **stainless:** configure calc and values endpoints ([165ad42](https://github.com/GRID-is/api-sdk-py/commit/165ad4236f257d68f25d60e367590de34fff054f))


### Chores

* **ci:** upload sdks to package manager ([7da0ed9](https://github.com/GRID-is/api-sdk-py/commit/7da0ed9be88b954c2ea315b46d61667040913601))

## 1.0.0 (2025-05-13)

Full Changelog: [v1.0.0-rc.9...v1.0.0](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.9...v1.0.0)

### Features

* **api:** api update ([9169dad](https://github.com/GRID-is/api-sdk-py/commit/9169dadf1222c8ac5ffdc2c87962aa51fde116a9))
* **api:** api update ([16ef1a8](https://github.com/GRID-is/api-sdk-py/commit/16ef1a81fbff57d845f76f34dde1fcd3a7ffc4d2))


### Bug Fixes

* **package:** support direct resource imports ([d1ae5b7](https://github.com/GRID-is/api-sdk-py/commit/d1ae5b7090a19875c90b0b82ffe613e87a7dfb16))
* **pydantic v1:** more robust ModelField.annotation check ([3ebe568](https://github.com/GRID-is/api-sdk-py/commit/3ebe568c76ea5a9cb661c3adaafb786616f89639))


### Chores

* broadly detect json family of content-type headers ([04db2e4](https://github.com/GRID-is/api-sdk-py/commit/04db2e4b38c1248f35eec3cdb2dc99c471aa0762))
* **ci:** add timeout thresholds for CI jobs ([5c76451](https://github.com/GRID-is/api-sdk-py/commit/5c76451b9350bc64be13a26641104cd9f4e369ed))
* **ci:** only use depot for staging repos ([5304e84](https://github.com/GRID-is/api-sdk-py/commit/5304e840bdd4ea5dac3b9c2269d80db47c2e6a20))
* **internal:** avoid errors for isinstance checks on proxies ([10c673b](https://github.com/GRID-is/api-sdk-py/commit/10c673b162551aba429fd5aaf83739c041d71a30))
* **internal:** codegen related update ([8831d75](https://github.com/GRID-is/api-sdk-py/commit/8831d75a26499b0df9df8c7ed32e69730b5b6177))
* **internal:** fix list file params ([a447537](https://github.com/GRID-is/api-sdk-py/commit/a447537d02ea1ad06fa0b24a6138cfab6818551d))
* **internal:** import reformatting ([500031e](https://github.com/GRID-is/api-sdk-py/commit/500031efa529a1422892e4137db74091ee66d1e7))
* **internal:** minor formatting changes ([929061c](https://github.com/GRID-is/api-sdk-py/commit/929061c95b05ef3c19b3bd9f5b8353e57f1b72b3))
* **internal:** refactor retries to not use recursion ([befb573](https://github.com/GRID-is/api-sdk-py/commit/befb573276a96eb4fef2128dd30ca45b9738e1de))

## 1.0.0-rc.9 (2025-04-19)

Full Changelog: [v1.0.0-rc.8...v1.0.0-rc.9](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.8...v1.0.0-rc.9)

### Chores

* **client:** minor internal fixes ([566fed9](https://github.com/GRID-is/api-sdk-py/commit/566fed90bf3cd2b4bcbb40e52107c6cecfb5f9b1))
* **internal:** base client updates ([c665a92](https://github.com/GRID-is/api-sdk-py/commit/c665a920b75380481bc8fbc43ca651807b58a7b0))
* **internal:** bump pyright version ([afe83fd](https://github.com/GRID-is/api-sdk-py/commit/afe83fd136a17f7fe4e6baf5a1a029e193fb6806))
* **internal:** update models test ([4c11f26](https://github.com/GRID-is/api-sdk-py/commit/4c11f2691818dda4d84373505d43460a99cc0619))
* **internal:** update pyright settings ([cc40184](https://github.com/GRID-is/api-sdk-py/commit/cc40184ddcb27d897140f173937af8a7264bec46))

## 1.0.0-rc.8 (2025-04-12)

Full Changelog: [v1.0.0-rc.7...v1.0.0-rc.8](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.7...v1.0.0-rc.8)

### Bug Fixes

* **perf:** optimize some hot paths ([398eb34](https://github.com/GRID-is/api-sdk-py/commit/398eb34c7ea0a12b62d024197137414c0783fc8e))
* **perf:** skip traversing types for NotGiven values ([eaef067](https://github.com/GRID-is/api-sdk-py/commit/eaef067e2c8263f40fb78455c2329642fe3907b8))

## 1.0.0-rc.7 (2025-04-11)

Full Changelog: [v1.0.0-rc.6...v1.0.0-rc.7](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.6...v1.0.0-rc.7)

### Features

* **api:** api update ([57475c7](https://github.com/GRID-is/api-sdk-py/commit/57475c765051f0d59e66a3cf798b7589d50dba44))

## 1.0.0-rc.6 (2025-04-10)

Full Changelog: [v1.0.0-rc.5...v1.0.0-rc.6](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.5...v1.0.0-rc.6)

### Chores

* **internal:** expand CI branch coverage ([f22e6d8](https://github.com/GRID-is/api-sdk-py/commit/f22e6d8c3e2bec48a2913b17dcd259101080ef3b))
* **internal:** reduce CI branch coverage ([3b9e183](https://github.com/GRID-is/api-sdk-py/commit/3b9e183586ba75a9bc328839cd2c615ef8ca813a))
* **internal:** slight transform perf improvement ([#34](https://github.com/GRID-is/api-sdk-py/issues/34)) ([d791043](https://github.com/GRID-is/api-sdk-py/commit/d7910433219333d4c4b30f3b6c32a71d5d843c3c))
* slight wording improvement in README ([#35](https://github.com/GRID-is/api-sdk-py/issues/35)) ([57af86f](https://github.com/GRID-is/api-sdk-py/commit/57af86f171c0b95b08bc75009d10aae2bcc920c1))

## 1.0.0-rc.5 (2025-04-05)

Full Changelog: [v1.0.0-rc.4...v1.0.0-rc.5](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.4...v1.0.0-rc.5)

### Chores

* **internal:** remove trailing character ([#32](https://github.com/GRID-is/api-sdk-py/issues/32)) ([151151a](https://github.com/GRID-is/api-sdk-py/commit/151151a3ca30ec80a14fbda35c5390e265c91a3d))


### Documentation

* swap examples used in readme ([#33](https://github.com/GRID-is/api-sdk-py/issues/33)) ([717e3d8](https://github.com/GRID-is/api-sdk-py/commit/717e3d8578f6d2871f5b493aa23f42d163563713))

## 1.0.0-rc.4 (2025-03-27)

Full Changelog: [v1.0.0-rc.3...v1.0.0-rc.4](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.3...v1.0.0-rc.4)

### Features

* **api:** finish renaming of HTTPBearer to apiKey ([#26](https://github.com/GRID-is/api-sdk-py/issues/26)) ([a504d33](https://github.com/GRID-is/api-sdk-py/commit/a504d33b95d33e6e43c80b43c055b18d7ad77256))

## 1.0.0-rc.3 (2025-03-27)

Full Changelog: [v1.0.0-rc.2...v1.0.0-rc.3](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.2...v1.0.0-rc.3)

### Features

* **api:** api update ([#21](https://github.com/GRID-is/api-sdk-py/issues/21)) ([1a10a2f](https://github.com/GRID-is/api-sdk-py/commit/1a10a2f7aa7c69d0cbe91465f36b962e64a34817))
* **api:** update API URL to api.grid.is ([#23](https://github.com/GRID-is/api-sdk-py/issues/23)) ([cb3d893](https://github.com/GRID-is/api-sdk-py/commit/cb3d893ce3f6fb2d3dd6d307d4a6a43bbedbe521))


### Bug Fixes

* **ci:** ensure pip is always available ([#19](https://github.com/GRID-is/api-sdk-py/issues/19)) ([90d7771](https://github.com/GRID-is/api-sdk-py/commit/90d7771b44b0bf487f8760917484a58b526f8556))
* **ci:** remove publishing patch ([#20](https://github.com/GRID-is/api-sdk-py/issues/20)) ([29c3e22](https://github.com/GRID-is/api-sdk-py/commit/29c3e22ebed4f4babd2ed53d1771b07c05f4fc07))
* **types:** handle more discriminated union shapes ([#17](https://github.com/GRID-is/api-sdk-py/issues/17)) ([1fb237f](https://github.com/GRID-is/api-sdk-py/commit/1fb237f8e027d1165bb99457a2969e6b07868ae6))


### Chores

* fix typos ([#24](https://github.com/GRID-is/api-sdk-py/issues/24)) ([2f17c6c](https://github.com/GRID-is/api-sdk-py/commit/2f17c6ca720129fd7c26a3b526e6bbe84426a09f))
* **internal:** bump rye to 0.44.0 ([#16](https://github.com/GRID-is/api-sdk-py/issues/16)) ([52a62dd](https://github.com/GRID-is/api-sdk-py/commit/52a62dd8e41083e4c197d9ed8ecef54d4767df9b))
* **internal:** codegen related update ([#10](https://github.com/GRID-is/api-sdk-py/issues/10)) ([5d60d51](https://github.com/GRID-is/api-sdk-py/commit/5d60d5133770437feb83d8f572e259bdc93d8836))
* **internal:** codegen related update ([#15](https://github.com/GRID-is/api-sdk-py/issues/15)) ([670ba69](https://github.com/GRID-is/api-sdk-py/commit/670ba698801fb44c225a57162a630cfeffa8ce7c))
* **internal:** remove extra empty newlines ([#14](https://github.com/GRID-is/api-sdk-py/issues/14)) ([02364c8](https://github.com/GRID-is/api-sdk-py/commit/02364c834cb819eba51f6efedc646942e0737b69))


### Documentation

* Explain how to use client api_key param ([8284d9e](https://github.com/GRID-is/api-sdk-py/commit/8284d9efa7618af844a50fa56c9edcd1f3a9c14d))
* Explain how to use client api_key param ([1e78269](https://github.com/GRID-is/api-sdk-py/commit/1e78269a70aaa215097bb0dd74f538291d8e92f1))

## 1.0.0-rc.2 (2025-03-07)

Full Changelog: [v1.0.0-rc.1...v1.0.0-rc.2](https://github.com/GRID-is/api-sdk-py/compare/v1.0.0-rc.1...v1.0.0-rc.2)

### Features

* **api:** update via SDK Studio ([#6](https://github.com/GRID-is/api-sdk-py/issues/6)) ([20f22bb](https://github.com/GRID-is/api-sdk-py/commit/20f22bb76d47a23e3986378380779ffcbc838c33))
* **api:** update via SDK Studio ([#7](https://github.com/GRID-is/api-sdk-py/issues/7)) ([4bfc5fc](https://github.com/GRID-is/api-sdk-py/commit/4bfc5fcf8a3e83559661497cf20a1f7055c1653c))
* **api:** update via SDK Studio ([#8](https://github.com/GRID-is/api-sdk-py/issues/8)) ([b3e0629](https://github.com/GRID-is/api-sdk-py/commit/b3e0629052e263fb71830963fbaa0dcc8757e1e0))

## 1.0.0-rc.1 (2025-03-07)

Full Changelog: [v0.0.1-alpha.0...v1.0.0-rc.1](https://github.com/GRID-is/api-sdk-py/compare/v0.0.1-alpha.0...v1.0.0-rc.1)

### Features

* **api:** update via SDK Studio ([1681f44](https://github.com/GRID-is/api-sdk-py/commit/1681f4461bbac77a7da643bc6f86ec5491cacaf3))
* **api:** update via SDK Studio ([16082e5](https://github.com/GRID-is/api-sdk-py/commit/16082e502dd15f83cfbd74d8ae665f66b9752bfd))
* **api:** update via SDK Studio ([b1bfbb0](https://github.com/GRID-is/api-sdk-py/commit/b1bfbb05bd74f7edfe4e0f1f86bc6efb4ca0b1f7))
* **api:** update via SDK Studio ([fc91744](https://github.com/GRID-is/api-sdk-py/commit/fc91744b75012c0fb4ec0a5f13cbdd1705b83c09))
* **api:** update via SDK Studio ([8a3fd46](https://github.com/GRID-is/api-sdk-py/commit/8a3fd4610f93b994ce5c5159827f41d97168f75b))
* **api:** update via SDK Studio ([b490b8e](https://github.com/GRID-is/api-sdk-py/commit/b490b8ecf3e14f10cbff8b98d3a4f76c77631f46))
* **api:** update via SDK Studio ([c585805](https://github.com/GRID-is/api-sdk-py/commit/c5858054647f40177fe49be04bafe6ad1d82e176))
* **api:** update via SDK Studio ([915590e](https://github.com/GRID-is/api-sdk-py/commit/915590e1bb76cb994ae81484ba6308ec4c80ef6d))
* **client:** allow passing `NotGiven` for body ([fd78717](https://github.com/GRID-is/api-sdk-py/commit/fd78717b5af5f16ef0408505fd6b21001acb70c9))
* Tweak text in README ([cf5e880](https://github.com/GRID-is/api-sdk-py/commit/cf5e880d94c2af5ec1070acf6590e3960a7b4c18))


### Bug Fixes

* asyncify on non-asyncio runtimes ([7ccd3fb](https://github.com/GRID-is/api-sdk-py/commit/7ccd3fb17c0180f74f77b9761a24e3e505e7eb37))
* **client:** mark some request bodies as optional ([fd78717](https://github.com/GRID-is/api-sdk-py/commit/fd78717b5af5f16ef0408505fd6b21001acb70c9))


### Chores

* **docs:** update client docstring ([022bf03](https://github.com/GRID-is/api-sdk-py/commit/022bf0374d3c338f9e823828e83123b98900f0ad))
* go live ([#1](https://github.com/GRID-is/api-sdk-py/issues/1)) ([994083f](https://github.com/GRID-is/api-sdk-py/commit/994083f57d84ade28b8ce11af19645c1bfd4e1b8))
* **internal:** fix devcontainers setup ([64c624a](https://github.com/GRID-is/api-sdk-py/commit/64c624a788b719ddbc043c70e2343962364cbba9))
* **internal:** properly set __pydantic_private__ ([b8abd6d](https://github.com/GRID-is/api-sdk-py/commit/b8abd6d321be4c6817cc47077973660f874ef8f9))
* **internal:** remove unused http client options forwarding ([b797666](https://github.com/GRID-is/api-sdk-py/commit/b797666f072ae10926aafb030dd8b0597f46aadc))
* **internal:** update client tests ([819795b](https://github.com/GRID-is/api-sdk-py/commit/819795b8f6d6c3e1376dd5d55de4e3354ae526b6))
* update SDK settings ([#3](https://github.com/GRID-is/api-sdk-py/issues/3)) ([ddac62b](https://github.com/GRID-is/api-sdk-py/commit/ddac62b7829177729de909ff2bd2a78badb2aa82))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([d340da6](https://github.com/GRID-is/api-sdk-py/commit/d340da60f579f93b048787d99306152c7b80c745))
