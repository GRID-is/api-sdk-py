# Changelog

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
