#### 实验内容：
AES impl with ARM instruction
#### 理论基础：
ARM Cryptography Extension: 在ARM架构中引入了用于加密和安全应用的指令集扩展。官方文档可以提供关于这些指令集的详细信息.https://developer.arm.com/architectures/instruction-sets/simd-isas/arm-crypto-extensions

ARM Cryptography Extension为ARM处理器提供了专门的AES指令，以加速AES的加密和解密操作。这些指令利用处理器内部的硬件加速器来执行AES算法中的基本操作，从而提高加密和解密的性能。

使用AES指令集可以提供硬件级别的优化，从而加速加密和解密过程，减少处理器的负载，并提高系统的安全性。ARM Cryptography Extension还提供其他的加密指令，如SHA-1和SHA-256哈希函数、3DES加密等，进一步增强了ARM架构上的密码学功能。

通过利用ARM处理器上的硬件加速AES指令集，开发人员可以实现高效且安全的AES加密算法，提高系统的性能和安全性，适用于诸如物联网设备、移动设备、网络设备和服务器等各种应用场景。
#### 实验思路：
(1)将AES密钥加载到AES密钥寄存器中。

(2)将明文数据加载到寄存器中。

(3)设置AES控制寄存器，指定加密/解密模式、密钥长度、输入和输出格式。

(4)调用AES指令执行加密/解密操作。

实验伪代码：(此伪代码源于网络)
```c
// 假设明文已加载到寄存器X0-X3
// 假设加密密钥已加载到寄存器X4-X7

// 设置加密模式、密钥长度和输入/输出格式
MOVI V0, 0x00000000  // 设置AESKEYR0（128位密钥的低32位）
MOVI V1, 0x00000000  // 设置AESKEYR1（128位密钥的高32位）
MOVI V2, 0x00000000  // 设置AESDINR（明文）
MOVI V3, 0x00000000  // 设置AESDOUTR（密文）

// 配置AES控制寄存器
MSR AESAKEYR0, V0
MSR AESAKEYR1, V1
MSR AESDINR, V2
MSR AESDOUTR, V3

// 执行AES加密
AESMC V4, V2

// 从AESDOUTR寄存器中提取密文
MRS V5, AESDOUTR
```
#### 实验结果：
