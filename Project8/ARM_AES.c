#include <arm_neon.h>
#include <stdio.h>

void aes_encrypt(const uint8_t* plaintext, const uint8_t* key, uint8_t* ciphertext)
{
    uint8x16_t block = vld1q_u8(plaintext);
    uint8x16_t key_schedule = vld1q_u8(key);
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaeseq_u8(block, key_schedule));
    block = vaesmcq_u8(vaesmcq_u8(vaeseq_u8(block, key_schedule)));
    vst1q_u8(ciphertext, block);
}

int main()
{
    uint8_t plaintext[16] = {0x32, 0x88, 0x31, 0xe0, 0x43, 0x5a, 0x31, 0x37, 0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34};
    uint8_t key[16] = {0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c};
    uint8_t ciphertext[16];

    aes_encrypt(plaintext, key, ciphertext);
    printf("m: ");
    for (int i = 0; i < 16; i++) {
        printf("%02x ", plaintext[i]);
    }
    printf("k: ");
    for (int i = 0; i < 16; i++) {
        printf("%02x ", key[i]);
    }
    printf("c: ");
    for (int i = 0; i < 16; i++) {
        printf("%02x ", ciphertext[i]);
    }
    printf("\n");

    return 0;
}
