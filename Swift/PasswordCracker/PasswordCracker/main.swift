//
//  main.swift
//  PasswordCracker
//
//  Created by Hare Sudhan Muthusamy on 9/19/19.
//  Copyright © 2019 Hare Sudhan Muthusamy. All rights reserved.
//

//#!/usr/bin/swift

import Foundation
// first argument is path to binary, drop it
let arguments = CommandLine.arguments.dropFirst()
if arguments.count > 0 {
    let argumentString = arguments.joined(separator: " ")
    print("Hello, \(argumentString)")
} else {
    print ("Hello, anybody!")
}
exit(0)

